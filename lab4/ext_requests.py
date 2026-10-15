import requests

def demo_requests(): # Створює функцію для перевірки мережевого з'єднання
    print("[requests] Спроба підключення до сайту...")
    try:
        response = requests.get("https://google.com", timeout=3)
        print(f"[requests] Код відповіді: {response.status_code}")
    except requests.RequestException as error:
        print(f"[requests] Перехоплено виключення: {error}")
    finally:
        print("[requests] Блок finally: перевірку завершено.")