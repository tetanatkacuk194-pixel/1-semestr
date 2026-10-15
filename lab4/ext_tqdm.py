import time
from tqdm import tqdm

def demo_tqdm():#Оголошує функцію для демонстрації прогресбару
    print("[tqdm] Рядок прогресу:")
    for _ in tqdm(range(3), desc="Обробка"):
        time.sleep(0.1)