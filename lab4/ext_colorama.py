from colorama import Fore, init

def demo_colorama():# Створює функцію для фарбування консолі
    init(autoreset=True)
    print(f"[colorama] {Fore.CYAN}Блакитний текст у консолі за PEP 8{Fore.RESET}")