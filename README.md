# Seed Moth Detection (Proof of Concept)

This repository contains a proof-of-concept for detecting moths in pheromone trap images using a YOLO-based model.
The goal is to demonstrate a viable approach under limited labeled data conditions.

## Project Structure

```
.
├── src/
│   ├── data_analysis.py
│   ├── labels_convertion.py
│   ├── train_test_split.py
│   ├── tuning_script.py
│   ├── train_yolo.py
│   └── predict.py
├── test_data_samples/
├── model/
│   └── best.pt
├── requirements.txt
└── README.md
```

* `src/` – contains all scripts used for data processing, training, tuning, and inference
* `test_data_samples/` – sample images for testing (Stenoma catenifer)
* `model/` – trained YOLO model weights (`best.pt`)
* `requirements.txt` – required Python dependencies

---

## Setup

Clone the repository and install dependencies:

```bash
git clone <repo-link>
cd <repo-name>
pip install -r requirements.txt
```

## Hardware

* The code supports both CPU and GPU execution
* If a CUDA-enabled GPU is available, it will be used automatically
* Otherwise, the code runs on CPU (slower performance)

---

## Data

Due to size limitations, the full dataset is not included.

The model was trained using:

* EU Moths dataset
* AMI dataset
