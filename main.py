import requests
from bs4 import BeautifulSoup


indeed_result = requests.get('https://www.indeed.com/jobs?q=python&limit=50')




def parsing_proc(result_val):

  indeed_soup = BeautifulSoup(result_val.text, "html.parser")
  
  pagination = indeed_soup.find("div", {"class": "pagination"})

  links = pagination.find_all('a')
  
  pages = []

  for link in links[:-1]:
  
    pages.append(int(link.string))


  
  max_page = pages[-1]
    

    


parsing_proc(indeed_result)