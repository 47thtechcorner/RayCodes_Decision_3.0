import os
import time
from transformers import AutoModel

def ask_choice(instructions: str, criteria: dict):
    return {"type": "choice", "instructions": instructions, "criteria": criteria}

def ask_yes_no(instructions: str):
    return {"type": "noul", "instructions": instructions}

def ask_score(instructions: str, levels: list):
    return {"type": "score", "instructions": instructions, "criteria": levels}

def run_decision_pipeline():
    os.makedirs("outputs", exist_ok=True)
    
    model_path = "models/d3-edge" if os.path.isdir("models/d3-edge") else "vllm-sr/d3-edge"
    print(f"[1/3] Loading Decision 3.0 model ({model_path})...")
    model = AutoModel.from_pretrained(model_path, trust_remote_code=True)
    
    receipt_img = os.path.join("inputs", "example-receipt.png")
    video_clip = os.path.join("inputs", "example-video.mp4")
    
    # Tough edge-case prompt: Subtle contradiction & multi-issue claim
    print("[2/3] Evaluating multimodal edge cases...")
    claim_state = "The customer claims the package arrived opened and the blender was broken, but says they already glued it back together and just want a partial store discount instead of a return."
    claim_queries = {
        "disposition": ask_choice(
            "What action should be taken given the customer altered the item?",
            {
                "standard_return": "Accept return and send full replacement",
                "voided_warranty_escalation": "Escalate to claims lead due to self-repair/alteration",
                "concession_credit": "Issue goodwill partial credit without physical return"
            }
        ),
        "item_match_on_receipt": ask_yes_no("Does the item line on the receipt explicitly match the claimed appliance model?"),
        "fraud_risk_score": ask_score(
            "Evaluate anomaly and policy override risk level:",
            ["Low_Standard", "Medium_Review", "High_Disputed"]
        )
    }
    
    t0 = time.perf_counter()
    claim_res = model.system_one(
        state=claim_state,
        images=[receipt_img] if os.path.exists(receipt_img) else None,
        questions=claim_queries
    )
    time_claim = (time.perf_counter() - t0) * 1000
    
    # Video edge-case: Sub-second visual anomaly & directional ambiguity
    video_state = "Rapid 2-second clip from automated sorting line inspection."
    video_queries = {
        "conveyor_trajectory": ask_choice(
            "Which direction does the tracked object travel across the frame?",
            {
                "downstream_right": "Exits to downstream right chute",
                "upstream_left": "Reverses or diverts to upstream left",
                "jammed_still": "Remains static or blocked"
            }
        ),
        "visual_color_shift": ask_yes_no("Does the object undergo an intentional optical color shift?"),
        "jam_severity": ask_score(
            "Rate blockage severity on the transport line:",
            ["Clear_Flow", "Advisory", "Critical_Jam"]
        )
    }
    
    t1 = time.perf_counter()
    video_res = model.system_one(
        state=video_state,
        videos=[video_clip] if os.path.exists(video_clip) else None,
        questions=video_queries
    )
    time_video = (time.perf_counter() - t1) * 1000
    
    # 3. Clean results-only output report
    print("[3/3] Writing results to outputs/outputs.md...")
    c_ans = claim_res.get("answers", {})
    v_ans = video_res.get("answers", {})
    
    def format_item(res_dict, key):
        item = res_dict.get(key, {})
        choice = item.get("choice", "N/A")
        prob = item.get("probabilities", {}).get(choice, 0.0)
        return f"`{choice}` ({prob * 100:.1f}% confidence)"
    
    report = f"""# Decision 3.0 Execution Results

## Multimodal Task: Claim & Receipt Evaluation
- Input: "{claim_state}"
- Attached Image: `inputs/example-receipt.png`
- Execution Time: {time_claim:.2f} ms

### Results
- Case Disposition: {format_item(c_ans, 'disposition')}
- Receipt Item Match: {format_item(c_ans, 'item_match_on_receipt')}
- Risk Assessment: {format_item(c_ans, 'fraud_risk_score')}

---

## Video Task: Conveyor Motion Inspection
- Input: "{video_state}"
- Attached Video: `inputs/example-video.mp4`
- Execution Time: {time_video:.2f} ms

### Results
- Conveyor Trajectory: {format_item(v_ans, 'conveyor_trajectory')}
- Color Shift Detected: {format_item(v_ans, 'visual_color_shift')}
- Jam Severity Rating: {format_item(v_ans, 'jam_severity')}
"""

    with open("outputs/outputs.md", "w", encoding="utf-8") as f:
        f.write(report)
        
    print("Done! Saved clean results to outputs/outputs.md")

if __name__ == "__main__":
    run_decision_pipeline()
