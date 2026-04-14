from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")
results = model.predict(source="runs/detect/Probe/predict6/142-20230123220000-snapshot.jpg", 
                        conf=0.2,save=True)
