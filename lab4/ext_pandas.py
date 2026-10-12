import pandas as pd

def demo_pandas():
    grades = list(range(4, 6))
    data = {"Студент": ["Іван", "Марія"], "Оцінка": grades}
    df = pd.DataFrame(data)
    print(f"[Pandas] DataFrame успішно ініціалізовано:\n{df.to_string()}")