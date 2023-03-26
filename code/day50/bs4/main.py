from bs4 import BeautifulSoup
import requests
import lxml
url = "https://news.ycombinator.com/newest"
#resonse
r = requests.get(url)

#text of webpage
web_text = r.text
soup = BeautifulSoup(web_text, "lxml")
all_box = soup.find_all(name="span",  class_="titleline")
titles = []
links = []

for data in all_box:
    title = data.find(name = "a")
    link = title.get("href")
    titles.append(title.text)
    links.append(link)
    

upvotes =  soup.find_all(name="span", class_="score")
upvotes_count = []
for upvote in upvotes:
    vote = int(upvote.get_text().split()[0]) #changing string upvote to integer
    
    upvotes_count.append(vote)
#printing out all title,link and url
for i in range(len(titles)):
    print(f"Title:{titles[i]}\nUpvote:{upvotes_count[i]}\nLink:{links[i]}\n\n")
#getting index of hihest upvote and printing out it title and link with number of upvotes
largest_upvote = max(upvotes_count)
largest_index = upvotes_count.index(largest_upvote)
print(f"Data with highest upvote:\nTitle:{titles[largest_index]}\nUpvote:{upvotes_count[largest_index]}\nLink:{links[largest_index]}")