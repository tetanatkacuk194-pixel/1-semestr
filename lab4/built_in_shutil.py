import shutil

def demo_shutil(): # Оголошує функцію для перевірки диска
    total, used, free = shutil.disk_usage(".")
    print(f"[shutil] Вільно на диску: {free // (2**30)} ГБ")