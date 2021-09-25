from bs4 import BeautifulSoup
from requests_html import HTMLSession


company = 'Apple Inc'
filing = '10-Q'
year = 2020
quarter = "QTR3"


def get_master_index(year,quarter):
    s = HTMLSession()
    master_index_url = f'https://www.sec.gov/Archives/edgar/full-index/{year}/{quarter}/master.idx'
    r = s.get(master_index_url).content
    master_index_decoded = r.decode("utf-8").split('\n')
    return master_index_decoded


def create_url_1(company, filing, master_index):
    for item in master_index:
        if (company in item) and (filing in item):
            company = item
            company = company.strip()
            company_item_split = company.split('|')
            url = company_item_split[-1]
            return url

def create_url_2(url_1):
    url_2 = url_1.split('-')
    url_2 = url_2[0] + url_2[1] + url_2[2]
    url_2 = url_2.split('.txt')[0]
    return url_2

def get_url(url_1, url_2):
    s = HTMLSession()
    html_site = 'https://www.sec.gov/Archives/' + url_1
    url_3 = s.get(html_site).content
    url_3 = url_3.decode('utf-8')
    url_3 = url_3.split('FILENAME>')
    url_3 = url_3[1].split('\n')[0]
    print(url_3)
    return 'https://www.sec.gov/Archives/' + url_2 + '/' + url_3

try:
    master_index = get_master_index(year=year, quarter= quarter)
except Exception:
    print("Master Index not found")

try:
    url_1 = create_url_1(company=company,filing=filing, master_index=master_index)
except Exception:
    print("url_1 was not able to be made")

try: 
    url_2 = create_url_2(url_1=url_1)
except Exception:
    print("url_2 was not able to be made")

try:
    final_url = get_url(url_1=url_1, url_2=url_2)
    print(final_url)
except Exception as e:
    print("final url was not able to be made")
    print(e)


