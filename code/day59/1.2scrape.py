# updated code to handle error 
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to be scraped
url = "https://kathmandupost.com/national/province-no-2"

# Making a request for parsing the website
r = requests.get(url)
time.sleep(1)                              # so that website is not overlaoded
soup = BeautifulSoup(r.text, "lxml")
articles = soup.find_all("article")

# Data list
data = []

# Function to extract article content
def get_article_content(url):
    article_class = "subscribe--wrapperx"                           # Update2: class of article
    date_class = "updated-time"                                     # Update3: class of date
    location_class = "updated-time updated-time_location"           # Update4: class of location

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        article_body = soup.find("div", class_=article_class).text.strip()
        article_date = soup.find("div", class_=date_class).text.strip()
        article_location = soup.find("div", class_=location_class).text.strip()
        article_content = [article_body, article_date, article_location]  # List containing article body, date, and location
        return article_content
    except Exception as e:
        print(f"Error occurred while scraping: {e}")
        return None

# Loop to get elements
for article in articles:
    try:
        article_title = article.find("h3").text.strip()                # Update5: article tag for title
        article_author = article.find("span").find("a").text.strip()   # Update6: article tag for author
        article_url = article.find("a")["href"]                        # Update6: article content link
        full_article_url = f"https://kathmandupost.com{article_url}"   # Update7: article content link update with the website
        article_content = get_article_content(full_article_url)        # Call function to get article content, date, location
        
        # Append data to the list
        data.append([article_title, *article_content, article_author])                 # List to append articles
    except Exception as e:
        print(f"Error occurred while processing article: {e}")
        data.append([article_title, None, None, None, None])  # If there's an error, add None values for article content, date, and location

# Create a DataFrame from the collected data
df = pd.DataFrame(data, columns=["Article Title", "Article Content", "Date", "Location","Author"])
print(df)
