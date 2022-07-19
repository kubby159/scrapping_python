import requests as req
from bs4 import BeautifulSoup as bs


LIMIT = 50
INDEED_URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'

def get_last_page():
    result = req.get(INDEED_URL)

    soup = bs(result.text, 'html.parser')


    pagination = soup.find('div',{'class': 'pagination'})

    links = pagination.find_all('a')
    pages = []
    for page in links[0:-1]:
        pages.append(int(page.string))

    max_page = pages[-1]

    return max_page



def extract_job(html):
        
        title = html.find('h2',{'class': 'jobTitle'}).string
        company = html.find('span',{'class': 'companyName'})
        company_anchor = company.find('a')
        location = html.find('div', {'class': 'companyLocation'})
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company  = company.string

        if location.string is not None:
            location = '정보없음'
        else:
            location = location.string


        return {"job_title" : title, "company_name": company, 'location' : location}
    



def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f'Scrapping  page : {page}')
        result =req.get(f'{INDEED_URL}&start={last_page*LIMIT}')
        soup = bs(result.text,'html.parser')
        results = soup.find_all('td',{'class':'resultContent'})
    
        for result in results:
            job  = extract_job(result)
            jobs.append(job)

    
    return jobs



def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs