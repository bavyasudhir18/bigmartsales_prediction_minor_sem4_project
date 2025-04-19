# E:\bigmart11\sales\utils.py

import requests
from bs4 import BeautifulSoup

def get_latest_headlines():
    url = "https://www.moneycontrol.com/news/business/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    headlines = []
    for link in soup.select(".clearfix a"):
        title = link.get_text(strip=True)
        if title:
            headlines.append(title)
        if len(headlines) == 5:
            break

    return headlines
