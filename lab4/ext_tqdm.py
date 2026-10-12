import time
from tqdm import tqdm

def demo_tqdm():
    print("[tqdm] Рядок прогресу:")
    for _ in tqdm(range(3), desc="Обробка"):
        time.sleep(0.1)