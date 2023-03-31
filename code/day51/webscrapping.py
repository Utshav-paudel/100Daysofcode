import requests
from bs4 import BeautifulSoup
#taking date from user
date = input("which year you like to travel type in YYYY-MM-DD format")
url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

song_titles = soup.find_all(name="li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")
titles = []
for song in song_titles:
    title = song.find(name="h3")
    titles.append(title.text.strip())
j=1
for i in titles:
    print(f"{j}.{i}")
    j+=1
