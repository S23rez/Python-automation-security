import requests
from bs4 import BeautifulSoup


def simple_scraper(url):
    print(f"--- Scraping Data from {url} ---")
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # This looks for all 'h2' titles - change to 'h3' or 'a' as needed
        items = soup.find_all('h2')
        for i, item in enumerate(items[:10]):
            print(f"{i + 1}. {item.get_text(strip=True)}")
    else:
        print("Failed to reach the site.")


# Usage:
simple_scraper("https://news.ycombinator.com/")