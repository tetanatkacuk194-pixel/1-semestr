from game_logic import AlchemyGame
from config import RECEPI, WIN_ZOLOTO, MAX_DAYS
def main(): print("=== RPG ALCHIMIK ===")
try:
    gra = AlchemyGame()
    while True:
        stan_gri = gra.check_status()
        if stan_gri == "WIN":
            print(f"\n🏆 PEREMOGA! Vi zvanyly laboratoriu! Zoloto: {gra.zoloto}")
            break
        elif stan_gri == "LOSE":
            print(f"\n💀 PROGRASH! Chas viishov, u vas lishe {gra.zoloto}/{WIN_ZOLOTO} zolota.")
            break
        print("\n1. stan | 2. receptu | 3. varutu | 4. prodatu | 5. vuhid")
        vbyr = input("Vvedit komandu: ").strip().lower()
        try:
            if vbyr == 'stan':
                print(f"\nDen: {gra.den}/{MAX_DAYS} | Zoloto: {gra.zoloto}/{WIN_ZOLOTO}")
                print(f"Ingredinti ({gra.inv_ing.get_info()}):")
                for k, v in gra.inv_ing.slots.items():
                    print(f"  {k}: {v}")
                print(f"Zillia ({gra.inv_pot.get_info()}):")
                for k, v in gra.inv_pot.slots.items():
                    print(f"  {k}: {v}")
            elif vbyr == 'receptu':
                for k, v in RECEPI.items():
                    print(f" {k} = {v[0]} + {v[1]}")
            elif vbyr == 'varutu':
                nomer = input("Vvedit nomer zillia (1-50): ").strip()
                gra.craft(f"Potion_{nomer}")
            elif vbyr == 'prodatu':
                gra.prodazh()
            elif vbyr == 'vuhid':
                break
            else:
                print("Neveerna komanda.")
        except Exception as e:
            print(f"Pomilka: {e}")
        else:
            print("Diu vykonano.")
        finally:
            print("---")
except Exception:
    print("Kritichna pomilka programy!")
finally:
    print("Programu zaversheno.")
if __name__ == "__main__":
    main()