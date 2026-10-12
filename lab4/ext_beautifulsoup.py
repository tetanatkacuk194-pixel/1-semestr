from bs4 import BeautifulSoup

def demo_beautifulsoup():
    soup = BeautifulSoup("<p>Hello World</p>", "html.parser")
    print(f"[BeautifulSoup] Знайдений текст: {soup.p.text}")