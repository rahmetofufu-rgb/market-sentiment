from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_hackernews(pages=5):
    all_titles = []
    for page in range(1, pages + 1):
        url = f"https://news.ycombinator.com/news?p={page}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        titles = [t.text for t in soup.select(".titleline a")]
        all_titles += titles
    return all_titles

def get_reuters():
    urls = [
        "https://www.reuters.com/world/",
        "https://www.reuters.com/markets/",
        "https://www.reuters.com/technology/"
    ]

    all_headlines = []

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    for url in urls:
        driver.get(url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        headlines = [h.get_text(strip=True) for h in soup.find_all("h3")]
        all_headlines += headlines

    driver.quit()
    return all_headlines

def get_bbc():
    urls = [
        "https://www.bbc.com/news",
        "https://www.bbc.com/news/business",
        "https://www.bbc.com/news/technology"
    ]

    all_headlines = []

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    for url in urls:
        driver.get(url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        headlines = [h.get_text(strip=True) for h in soup.find_all("h3")]
        all_headlines += headlines

    driver.quit()
    return all_headlines

def get_all_headlines():
    all_headlines = []
    all_headlines += get_hackernews(pages=5)
    all_headlines += get_reuters()
    all_headlines += get_bbc()
    return all_headlines

if __name__ == "__main__":
    headlines = get_all_headlines()
    print("Total headlines:", len(headlines))
    for i, h in enumerate(headlines[:10], 1):
        print(f"{i}. {h}")