# import all required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
#url of website to be scrapped
url="https://www.iplt20.com/auction/2022"
#making request for parsing website
r=requests.get(url)
#getting all text file that is html
soup=BeautifulSoup(r.text,"lxml")
#now we will be selective and extract data we want from this html file
#first we will find table of data
table=soup.find("table",class_="ih-td-tab auction-tbl")
#finding title of table
title=table.find_all("th",class_="skip-filter")
#put all title in list
header=[]
for i in title:
    name=i.text 
    header.append(name)
#creating a dataframe by passing header
df=pd.DataFrame(columns=header)
#now we will get data from rows of table 
rows=table.find_all("tr")
for i in rows[1:]:
    first_td=i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()
    data=i.find_all("td")[1:]
    row=[tr.text for tr in data]
    row.insert(0,first_td)
    l=len(df)
    df.loc[l]=row 
df.to_csv("ipl auction stats.csv")