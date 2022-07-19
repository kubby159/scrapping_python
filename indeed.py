import requests as req
from bs4 import BeautifulSoup as bs


LIMIT = 50
INDEED_URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'

def extract_indeed_pages():
    result = req.get(INDEED_URL)

    soup = bs(result.text, 'html.parser')


    pagination = soup.find('div',{'class': 'pagination'})

    links = pagination.find_all('a')
    pages = []
    for page in links[0:-1]:
        pages.append(int(page.string))

    max_page = pages[-1]

    return max_page



def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result =req.get(f'{INDEED_URL}&start={0*LIMIT}')
    soup = bs(result.text,'html.parser')
    results = soup.find_all('td',{'class':'resultContent'})
    
    for result in results:
        title = result.find('h2',{'class': 'jobTitle'})
        company = result.find('span',{'class': 'companyName'})
        if company.find('a') is not None:
            print(company.find('a').string)
        else:
            print(company.string)
    
      
      

    
   

    
    return jobs
