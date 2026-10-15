from built_in_os import demo_os
from built_in_sys import demo_sys
from built_in_shutil import demo_shutil
from built_in_math import demo_math
from built_in_json import demo_json
from ext_numpy import demo_numpy
from ext_pandas import demo_pandas
from ext_requests import demo_requests
from ext_pillow import demo_pillow
from ext_tqdm import demo_tqdm
from ext_colorama import demo_colorama
from ext_pydantic import demo_pydantic
from ext_beautifulsoup import demo_beautifulsoup
from ext_matplotlib import demo_matplotlib
from ext_art import demo_art
def main():#Ствоює головну функцію
    print("=== ЗАПУСК ЛАБОРАТОРНОЇ РОБОТИ ===\n")
    demo_os()
    demo_sys()
    demo_shutil()
    demo_math()
    demo_json()
    demo_numpy()
    demo_pandas()
    demo_requests()
    demo_pillow()
    demo_tqdm()
    demo_colorama()
    demo_pydantic()
    demo_beautifulsoup()
    demo_matplotlib()
    demo_art()
    print("\n=== Всі 15 модулів відпрацювали успішно! ===")
if __name__ == "__main__":
    main()