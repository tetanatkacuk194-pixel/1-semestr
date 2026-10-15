from PIL import Image

def demo_pillow(): # Оголшує функцію для малювання картинок
    img = Image.new("RGB", (50, 50), color="green")
    print(f"[Pillow] Створено пусте зображення: {img.size}")