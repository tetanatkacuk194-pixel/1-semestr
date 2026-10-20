import random
from config import INGREDIENTS_POOL, POTIONS_POOL, RECEPI, WIN_ZOLOTO, MAX_DAYS, DAILY_ING
from inventory import LimitedInventory
class AlchemyGame:
    def __init__(self):
        self.den = 1
        self.zoloto = 0
        self.inv_ing = LimitedInventory(25, 25)
        self.inv_pot = LimitedInventory(10, 10)
        self.start_day()
    def start_day(self):
        try:
            print(f"\n--- Ranok dnia {self.den} ---")
            all_ing = list(INGREDIENTS_POOL.keys())
            for _ in range(DAILY_ING):
                shos = random.choice(all_ing)
                try:
                    self.inv_ing.add_item(shos, 1)
                    print(f" + {shos}")
                except IndexError:
                    print(f" [!] Vpalo na pidlogu: {shos}")
        except Exception:
            print("Pomilka dnia.")
    def craft(self, pot_name):
        try:
            if pot_name not in RECEPI:
               print("Nemae take.")
               return
            potribno = RECEPI[pot_name]
            for ing in potribno:
                if ing not in self.inv_ing.slots or self.inv_ing.slots[ing] < 1:
                    raise KeyError()
            try:
               self.inv_pot.add_item(pot_name, 1)
            except IndexError:
                print("Nemae mistsa dlia zillia!")
                return
            for ing in potribno:
                self.inv_ing.remove_item(ing, 1)

            print(f" [Ok] Zvareno: {pot_name}")
        except KeyError:
            print("Nedoztathno ingredientiv dlia kraftu.")
        except Exception:
            print("Shos pishlo ne tak.")
    def prodazh(self):
        try:
           print("\n--- Vechirniy prodazh ---")
           vsego_zarobiv = 0
           spisok_pot = list(self.inv_pot.slots.keys())
           if not spisok_pot:
               print("Nemae zillia na prodazh.")
               return
           for pot in spisok_pot:
               kilkist = self.inv_pot.slots[pot]
               cina = POTIONS_POOL[pot]
               vsego_zarobiv += kilkist * cina
               self.inv_pot.remove_item(pot, kilkist)
               print(f"Prodano {pot} x{kilkist} za {kilkist * cina}")
           self.zoloto += vsego_zarobiv
           print(f"Zarobleno: {vsego_zarobiv}. Balans: {self.zoloto}")
        except Exception:
           print("Pomilka prodazhu.")
        finally:
            if self.zoloto < WIN_ZOLOTO and self.den < MAX_DAYS:
                self.den += 1
                self.start_day()
    def check_status(self):
        if self.zoloto >= WIN_ZOLOTO:
            return "WIN"
        if self.den >= MAX_DAYS:
            return "LOSE"
        return "PLAY"