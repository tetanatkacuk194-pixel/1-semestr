import random
INGREDIENTS_POOL = {}
for i in range(1, 205):
    INGREDIENTS_POOL[f"Ingredient_{i}"] = random.randint(5, 20)
POTIONS_POOL = {}
for i in range(1, 51):
    POTIONS_POOL[f"Potion_{i}"] = random.randint(40, 150)
RECEPI = {}
ing_list = list(INGREDIENTS_POOL.keys())
for i in range(1, 51):
    ing1 = ing_list[(i * 3) % len(ing_list)]
    ing2 = ing_list[(i * 7) % len(ing_list)]
    RECEPI[f"Potion_{i}"] = [ing1, ing2]
WIN_ZOLOTO = 1000
MAX_DAYS = 10
DAILY_ING = 5