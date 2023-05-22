from scrapers.indeed import extract_indeed_jobs
from scrapers.weworkremotely import extract_wwr_jobs
keyword = input("What is your job search? ")
file = open(f"{keyword}.csv", "w")

file.write("Position,Company,Location,URL\n")


#indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs =  wwr
for job in jobs:
  file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")
file.close()

