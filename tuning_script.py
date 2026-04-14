from ultralytics import YOLO

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")
trainable_model = YOLO('yolo26n.pt')

# Define search space
search_space = {
    "lr0": (1e-4, 1e-1),
    "weight_decay": (0.0, 0.001),
    "warmup_epochs":(0.0, 5.0),
    "hsv_s": (0.0, 0.9),
    "hsv_v":(0.0, 0.9),
    "fliplr":(0.0, 1),
    "flipud":(0.0, 1),
    "degrees":(0.0,45),
    "shear":(0.0, 10),
    "scale":(0.0,0.9),
    "copy_paste":(0.0,1),
    "mixup":(0.0, 1.0)
}

trainable_model.tune(
    data="data.yaml",
    epochs=50,
    iterations=50,
    optimizer="AdamW",
    space=search_space,
    plots=False,
    save=False,
    val=False,
    device=device
)
