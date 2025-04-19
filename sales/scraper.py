import requests
from bs4 import BeautifulSoup

def scrape_latest_sales_news():
    url = 'https://www.investing.com/news/stock-market-news'  # example URL
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.select('.textDiv a.title')[:5]  # adjust selector

    news_list = []
    for article in articles:
        title = article.get_text(strip=True)
        link = 'https://www.investing.com' + article['href']
        news_list.append({'title': title, 'link': link})
    
    return news_list
