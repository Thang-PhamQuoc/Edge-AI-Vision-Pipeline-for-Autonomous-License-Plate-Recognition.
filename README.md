# Edge AI Vision Pipeline for Autonomous License Plate Recognition 

An end-to-end Edge AI vision pipeline for ALPR. Integrates YOLO for robust ROI localization and PaddleOCR (CRNN+CTC) for sequence decoding. Features a Tkinter-based local server, Regex heuristic filters, and automated CSV telemetry logging.

## Key Features
*   **Two-Stage Vision Pipeline:** Combines YOLOv8 for high-precision bounding box detection and PaddleOCR for accurate text extraction.
*   **Edge-Optimized Dashboard:** A lightweight Tkinter GUI designed for local Edge servers, ensuring real-time monitoring without cloud dependency.
*   **Anti-Hallucination Regex Filter:** Implements heuristic rules specifically tailored for Vietnamese license plate syntax to mitigate OCR reading errors.
*   **Automated Telemetry Logging:** Automatically logs validated plates and exact timestamps into CSV databases for smart parking management.

## 📊 System Performance & Results

### 1. Dashboard Interface
![ALPR Dashboard Demo](https://cdn.phototourl.com/free/2026-06-20-48654cc7-5f4e-48e5-90ab-38ab185d8e5e.jpg)

### 2. Training Metrics
The YOLO object detection model was trained robustly. Below are the Accuracy and Loss validation curves over the training epochs:

<p align="center">
  <img src="https://cdn.phototourl.com/free/2026-06-20-e5d2c45a-122c-4cd7-8e77-9b9c4ec98056.png" width="48%" alt="Accuracy Curve" />
  <img src="https://cdn.phototourl.com/free/2026-06-20-053eaf25-ec35-463b-9d0b-37c4eefd6db6.png" width="48%" alt="Loss Curve" />
</p>



Author
Pham Quoc Thang

Major: Electronics & Telecommunication Engineering

LinkedIn: thang-pham-quoc-238663332

GitHub: @Thang-PhamQuoc
