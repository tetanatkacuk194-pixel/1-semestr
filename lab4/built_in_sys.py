import sys

def demo_sys(): #Створює функцію для зчитування системних даних
    version_python= sys.version
    systema = sys.platform
    print(f"[sys] Версія Python: {version_python} на платформі {systema}")