<div align="center">
  <a href="https://youtu.be/PoXEu6tDhes">
    <img src="https://img.youtube.com/vi/PoXEu6tDhes/0.jpg" alt="Decision 3.0 Dropped: #1 Jev Index AI That Analyzes Videos!">
  </a>
  <h3>📺 <a href="https://youtu.be/PoXEu6tDhes">Watch the full tutorial on YouTube</a></h3>
</div>

# 🔮 Decision 3.0 Multimodal Router

Lightning-fast zero-shot decision engine that classifies text, images, and videos in milliseconds without text generation delay.

| Step 1: Input | Step 2: AI Action | Step 3: Result |
| :--- | :--- | :--- |
| Text, receipt images, or video clips | Unified 0.59B model processes input and questions | Instant routing choices, flags, and urgency scores |

---

## ⚡ Superpowers

- **Microsecond Routing**: Makes decisions in 6.7 ms directly through classifier heads without generating chat words.
- **Multimodal Ingestion**: Analyzes text state, high-resolution receipt images, and security video clips in one pass.
- **Python Question Builders**: Configure choice questions, yes/no flags, and numerical scales via intuitive python helper methods.
- **Calibrated Probabilities**: Returns direct confidence scores for every option to guarantee predictable automation.
- **Apache-2.0 License**: Fully open model architecture built on top of Qwen3.5-0.8B for edge and cloud deployment.

---

## 🛠️ Tech Stack

- **Model Engine**: `vllm-sr/d3-edge` (0.59B Multimodal Foundation Decision Model)
- **Base Architecture**: Qwen3.5-0.8B with integrated 0.10B vision encoder
- **Core Libraries**: `transformers==5.17.0`, `torch`, `torchvision`, `pillow`, `opencv-python-headless`, `safetensors`, `accelerate`
- **Inference Runtime**: Python 3.10+ / PyTorch

---

## 🚀 Setup & Installation

Install all required dependencies:

```powershell
pip install "transformers==5.17.0" torch torchvision pillow opencv-python-headless safetensors accelerate huggingface_hub
```

Download the official model weights into the `models/` directory:

```powershell
hf download vllm-sr/d3-edge --local-dir models/d3-edge
```

---

## 💻 Quickstart Execution

Run the multimodal triage pipeline:

```powershell
python main.py
```

The router inspects the incoming text scenario, attached receipt photo (`inputs/example-receipt.png`), and video clip (`inputs/example-video.mp4`), measures execution latency, and logs structured decisions into `outputs/outputs.md`.

---

## 📂 Source Structure

```text
├── inputs/
│   ├── example-receipt.png
│   └── example-video.mp4
├── models/
│   └── d3-edge.safetensors
├── main.py
└── README.md
```

- `inputs/`: Multimodal sample inputs (receipt image and surveillance video clip).
- `models/`: Local model checkpoint repository.
- `main.py`: Production pipeline executing multimodal decision queries.
- `README.md`: Complete documentation and quickstart instructions.

---

## 🎯 5 Practical Use Cases

1. **E-Commerce Return Routing**: Automatically checks customer claims against uploaded receipt photos and routes urgent replacement requests to warehouse specialists.
2. **Security Camera Triage**: Classifies moving objects or color changes in live surveillance clips and triggers immediate alerts.
3. **Medical Form Verification**: Validates patient symptom questionnaires and cross-checks attached prescription photos before doctor triage.
4. **Loan Application Pre-Screening**: Evaluates applicant financial states alongside identity card photos to score approval urgency.
5. **Smart Factory Quality Control**: Inspects assembly line sensor logs and machine video feeds to identify mechanical faults.

---

## 🔮 5 Future Expansions

1. **Audio Stream Decision Heads**: Ingest spoken call recordings alongside video and text for omni-channel customer support.
2. **Local GGUF Quantization Support**: Quantize weights into 4-bit formats for direct execution on microcontrollers and smart cameras.
3. **Dynamic Question Caching**: Cache key questions and prompt embeddings across sessions for sub-millisecond dispatching.
4. **Custom Adapter Fine-Tuning**: Allow domain-specific classifier head tuning on proprietary enterprise ticketing data.
5. **Live Multi-Stream Camera Pipeline**: Scale the decision engine across concurrent RTSP video feeds simultaneously.

---

## 🏷️ Keywords & Tags

`Decision 3.0` `vllm-sr/d3` `Jev Index` `vLLM` `Multimodal AI` `Fast AI Routing` `Zero Shot Decision Model` `Video Analysis AI` `Vision Classifier` `Edge AI` `Qwen Vision` `Microsecond AI`

