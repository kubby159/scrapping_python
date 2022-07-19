import requests as req
from bs4 import BeautifulSoup as bs



URL = f'https://stackoverflow.com/jobs/companies?tl=python'


def get_last_page():
    res = req.get(URL)
    soup = bs(res.text,'html.parser')
    results = soup.find('div',{'class': 's-pagination'}).find_all('a',{'class':'s-pagination--item'})
    pages = []
    for result in results[:-1]:
        pagenation = result.find('span').string
        pages.append(int(pagenation))

    
    return pages

def get_jobs():
    last_page = get_last_page()
    print(last_page)
    return last_page





