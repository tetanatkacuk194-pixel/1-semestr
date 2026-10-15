import numpy as np

def demo_numpy():#Оголошує функцію для роботи з масивами
    matrix = np.arange(1, 5).reshape(2, 2)
    print(f"[NumPy] Масив створено. Форма масиву: {matrix.shape}")