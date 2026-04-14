import json
import os
from pathlib import Path

CLASS_MAP = {
    "moth": 0,
    "no_moth": 1
}

def convert_json_to_yolo(json_path, output_dir):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    img_w = data["imageWidth"]
    img_h = data["imageHeight"]

    yolo_lines = []

    for shape in data["shapes"]:
        label = shape["label"]
        points = shape["points"]

        x1, y1 = points[0]
        x2, y2 = points[1]

        x_center = ((x1 + x2) / 2) / img_w
        y_center = ((y1 + y2) / 2) / img_h
        width    = abs(x2 - x1) / img_w
        height   = abs(y2 - y1) / img_h

        class_id = CLASS_MAP.get(label, -1)
        if class_id == -1:
            print(f"  [SKIP] Nepoznata klasa: {label} u {json_path.name}")
            continue

        yolo_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

    if not yolo_lines:
        print(f"  [EMPTY] Nema validnih labela: {json_path.name}")
        return

    base_name   = json_path.stem
    output_path = Path(output_dir) / (base_name + ".txt")

    with open(output_path, "w") as f:
        f.write("\n".join(yolo_lines))

    print(f"  [OK] {output_path.name}")


def batch_convert(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    json_files = list(Path(input_dir).rglob("*.json"))
    print(f"Pronadjeno {len(json_files)} JSON fajlova\n")

    for json_path in json_files:
        convert_json_to_yolo(json_path, output_dir)

    print(f"\nZavrseno. TXT fajlovi su u: {output_dir}")


if __name__ == "__main__":
    input_folder  = r"moth_images_splited\train"
    output_folder = "labels_yolo_train"

    batch_convert(input_folder, output_folder)