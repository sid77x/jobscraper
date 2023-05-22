from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)
result= []
def extract_indeed_jobs(keyword):
  
  search_term = keyword
  base_url = 'https://in.indeed.com/jobs?q='
  
  url = f'{base_url}{search_term}'
  browser.get(url)
  response = browser.page_source
  soup = BeautifulSoup(response, "html.parser")
  job_list = soup.find('ul', class_="jobsearch-ResultsList")
  jobs = job_list.find_all('li', recursive=False)
  for job in jobs:
    zone = job.find('div', class_="mosaic-zone")
    if zone == None:
      h2 = job.find('h2', class_='jobTitle')
      a = h2.find('a')
      title = a['aria-label']
      link = a['href']
     # print("Title: ", title[16:])
      name = job.find('span', class_="companyName").string
     # print("Company:", name)
     # print("Link: ", f'https://in.indeed.com{link}')
      location = job.find('div', class_="companyLocation").string
     # print("Location: ", location)
      job_data={
        'link' : f'https://in.indeed.com{link}',
        'company' : name[16:],
        'position' : title,
        'location' : location
      }
      result.append(job_data)
      
      
      #print("///////////////\n")
  return result
