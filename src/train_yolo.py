from ultralytics import YOLO
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")


model = YOLO("yolo26n.pt")  

model.train(
    data="data.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    pretrained = True,
    device = device,

    lr0=0.0005,
    weight_decay=0.00088,
    warmup_epochs=1.80982,
    hsv_s=0.42428,
    hsv_v=0.38439,
    fliplr=0.40306,
    flipud=0.00245,
    degrees=0.01807,
    shear=0.00068,
    scale=0.73987,
    copy_paste=0.00214,
    mixup=0.01777
)