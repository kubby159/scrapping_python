import requests as req
from bs4 import BeautifulSoup as bs
indeed_result  =  req.get('https://kr.indeed.com/jobs?q=%EC%A4%91%EC%86%8C%EA%B8%B0%EC%97%85&l=%EC%9D%B8%EC%B2%9C&vjk=31d2f80f34bb3961')
# indeed_result.text : html 가져오기

soup = bs(indeed_result.text, 'html.parser')
pagination = soup.find('div',{'class' : 'pagination'})

pages = pagination.find_all('a')

spans = []
for page in pages:
    spans.append(page.find('span'))


print(spans[:-1])