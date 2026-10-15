import json

def demo_json(): #Створює функцію для показання як працює бібліотека
    data = {"status": "success", "lab": 4}
    json_str = json.dumps(data)
    print(f"[json] Рядок JSON: {json_str}")