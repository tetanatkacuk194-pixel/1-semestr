import shutil

def demo_shutil():
    total, used, free = shutil.disk_usage(".")
    print(f"[shutil] Вільно на диску: {free // (2**30)} ГБ")