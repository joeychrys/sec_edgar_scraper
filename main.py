from bs4 import BeautifulSoup
import requests

def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


url = "https://www.sec.gov/ix?doc=/Archives/edgar/data/320193/000032019321000065/aapl-20210626.htm#ibbf5b20ab76c4c71bb743a1e5da969e3_13"
soup = get_soup(url=url)
print(soup)