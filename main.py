import requests
from bs4 import BeautifulSoup


indeed_result = requests.get('https://www.indeed.com/jobs?q=python&limit=50')


spans = []

def parsing_proc(result_val):

  indeed_soup = BeautifulSoup(result_val.text, "html.parser")
  
  pagination = indeed_soup.find("ul", {"class": "pagination-list"})

  pages = pagination.find_all('a')
  
  temp_spans = []

  for page in pages:
  
    temp_spans.append(page.find('span'))


  print(temp_spans[:-1])

    

    


parsing_proc(indeed_result)