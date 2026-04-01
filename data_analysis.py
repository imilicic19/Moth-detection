import os
import matplotlib.pyplot as plt

class_counts = {}

for class_name in os.listdir("images"):
    class_path = os.path.join("images", class_name)
    if os.path.isdir(class_path):
        imgs = [f for f in os.listdir(class_path) 
                if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        class_counts[class_name] = len(imgs)

sorted_counts = sorted(class_counts.items(), key=lambda x: x[1])
names = [x[0] for x in sorted_counts]
counts = [x[1] for x in sorted_counts]

plt.figure(figsize=(20, 6))
plt.bar(range(len(counts)), counts)
plt.xlabel("Klasa")
plt.ylabel("Broj slika")
plt.title("Distribucija slika po klasama")
plt.xticks(range(len(names)), names, rotation=90, fontsize=5)
plt.axhline(y=sum(counts)/len(counts), color='red', linestyle='--', label=f"Prosek: {sum(counts)/len(counts):.1f}")
plt.legend()
plt.tight_layout()
plt.show()