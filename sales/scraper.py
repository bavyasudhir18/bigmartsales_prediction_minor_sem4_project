import requests
from bs4 import BeautifulSoup

def scrape_latest_sales_news():
    url = 'https://www.moneycontrol.com/news/business/markets/'  # more scraper-friendly site
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch page, status code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.select('li.clearfix a')[:5]  # adjust selector as needed

        news_list = []
        for article in articles:
            title = article.get_text(strip=True)
            link = article.get('href')
            if title and link:
                news_list.append({'title': title, 'link': link})

        return news_list

    except Exception as e:
        print(f"Scraping failed: {e}")
        return []
