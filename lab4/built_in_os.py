import os

def demo_os(): #Створює функцію для перевірки системних папок
    current_dir = os.getcwd()
    print(f"[os] Поточна робоча директорія: {current_dir}")