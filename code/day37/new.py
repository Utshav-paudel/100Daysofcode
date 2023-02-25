import requests
from bs4 import BeautifulSoup
import pandas as pd
# make a request to the webpage containing the data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
r = requests.get(url)
# create a BeautifulSoup object
soup = BeautifulSoup(r.content, "html.parser")
# find the table containing the data
tables = soup.find_all("table", class_ = 'historical_data_table table')
table = tables[1]
# extract the table headers
headers = []
for th in table.find_all("th"):
    headers.append(th.text.strip())
# extract the table rows
rows = []
for tr in table.find_all("tr"):
    row = []
    for td in tr.find_all("td"):
        row.append(td.text.strip())
    if row:
        rows.append(row)
# # create a pandas dataframe
df = pd.DataFrame(rows, columns= ['Date','Revenue'])
df.to_csv('tesla_revenue.csv')
print(df)