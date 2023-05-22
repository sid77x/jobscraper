import requests
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  search_term = keyword 

  final_url = f'{base_url}{search_term}' 
  response = requests.get(final_url)
 # print(final_url)
  results = []
  if(response.status_code!= 200):
    print("Website down")
  else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_ = "jobs")
    for job_section in jobs:
      job_posts = job_section.find_all('li', class_ = 'feature')
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        job_link = anchor['href']
        company, type, region = anchor.find_all('span', class_ = "company")    
        title = anchor.find('span', class_ = "title")
      #  print("Position: ",title.string)
       # print("Company: ", company.string)
     #   print("Type: ", type.string)
      #  print("Region: ", region.string)
      #  print("\\\\\\\\\\///")
      job_data = {
        'position' : title.string,
        'company' : company.string,
        'location' : region.string,
        'link': f'https://weworkremotely.com/{job_link}'

        
        
      }
      results.append(job_data)
    
    return results
