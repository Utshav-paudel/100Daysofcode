from bs4 import BeautifulSoup
import requests
url = "https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35"

html_text = requests.get(url)
soup = BeautifulSoup(html_text.text, 'lxml')

jobs = soup.find_all('li' , class_ = "clearfix job-bx wht-shd-bx")
joblist=[]
for job in jobs:
    jobname = job.find('a').text
    skills = job.find('span' , class_='srp-skills').text.replace(' ','')   
    posstedtime = job.find('span', class_='sim-posted').span.text
    print(f'''
    Jobname ={jobname}
    skills = {skills}
    posted time = {posstedtime}
    ''')




