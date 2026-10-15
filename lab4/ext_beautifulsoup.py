from bs4 import BeautifulSoup

def demo_beautifulsoup():# Оголошує функцію для вирізання тегів
    soup = BeautifulSoup("<p>Hello World</p>", "html.parser")
    print(f"[BeautifulSoup] Знайдений текст: {soup.p.text}")