import shutil
from pathlib import Path

def create_yolo_structure(image_source_dir, labels_source_dir, output_dir):
    """
    image_source_dir  — folder sa originalnim slikama (sa podfodlerima po klasama)
    labels_source_dir — folder sa konvertovanim TXT fajlovima
    output_dir        — destinacija: test/images i test/labels
    """
    images_out = Path(output_dir) / "images"
    labels_out = Path(output_dir) / "labels"
    images_out.mkdir(parents=True, exist_ok=True)
    labels_out.mkdir(parents=True, exist_ok=True)

    # Pronađi sve slike rekurzivno
    image_paths = list(Path(image_source_dir).rglob("*.jpg")) + \
                  list(Path(image_source_dir).rglob("*.png"))

    print(f"Pronadjeno {len(image_paths)} slika\n")

    copied, missing_label = 0, 0

    for img_path in image_paths:
        # Pronađi odgovarajući TXT fajl
        txt_path = Path(labels_source_dir) / (img_path.stem + ".txt")

        if not txt_path.exists():
            print(f"  [MISS] Nema labele za: {img_path.name}")
            missing_label += 1
            continue

        # Kopiraj sliku i labelu
        shutil.copy(img_path, images_out / img_path.name)
        shutil.copy(txt_path, labels_out / txt_path.name)
        copied += 1

    print(f"\nZavrseno:")
    print(f"  Kopirano:       {copied} parova (slika + labela)")
    print(f"  Bez labele:     {missing_label} slika")
    print(f"\nStruktura kreirana u: {output_dir}")


if __name__ == "__main__":
    create_yolo_structure(
        image_source_dir  = r"moth_images_splited\train",   
        labels_source_dir = "labels_yolo_train",                  
        output_dir        = r"yolo_dataset\train"
    )
