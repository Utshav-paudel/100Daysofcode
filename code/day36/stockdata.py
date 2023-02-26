from bs4 import BeautifulSoup
import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')


table = soup.find_all('table', class_ ='historical_data_table table')

for i in table:
    print(i.text)

