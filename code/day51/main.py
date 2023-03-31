import requests
#authenication
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://mysite.com/callback/",
        client_id="57ccfc71faf04c6db3a2905da04ced14",
        client_secret="cd48146c579946bb9e3f39746b251d5d",
        show_dialog=True,
        cache_path="token.txt"
    )
)

#searching 
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#

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

print(titles)

#spotify authenication
spotify_auth = spotipy.oauth2.SpotifyOAuth(client_id=Client_ID,
client_secret=Client_Secret,
redirect_uri=redirect_URI,
scope="playlist-modify-private",
show_dialog=True,
cache_path="token.txt"
)
spotify_auth.get_access_token(as_dict=False)
s = spotipy.Spotify(oauth_manager=spotify_auth)
user_id = s.current_user()["id"]
print (user_id) #printing user id

