from ultralytics import YOLO
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

model = YOLO("runs/detect/train/weights/best.pt")

results = model.predict(
    source="original (2).jpg",
    conf=0.2,
    save=True,
    device=device
)
