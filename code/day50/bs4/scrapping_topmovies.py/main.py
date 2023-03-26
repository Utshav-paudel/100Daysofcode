from bs4 import BeautifulSoup
import requests
url = "https://www.timeout.com/film/best-movies-of-all-time"
r = requests.get(url)

soup=BeautifulSoup(r.text , "html.parser")

#getting required data
# datas = soup.find_all(name="h3", class_="jsx-4245974604")
datas = soup.find_all(name="h3",class_="_h3_cuogz_1")
list = []
for data in datas:
    movies=data.text
    list.append(movies)

import pandas as pd  
df = pd.DataFrame(list)
print(df.head(5))
print(df.columns)

#df.to_csv("movieslist.csv")
