from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Users\utsha\OneDrive\Desktop\chrome driver\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")
# selecting item to be fetched
date = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last time")
titles = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last .menu a")
#creating dictionary
events = {}
for n in range(len(date)):
    events[n] = {
        "time":date[n].text,
        "name":titles[n].text,
    }
#using dict comphrension
# events = {
#     n: {"time": date[n].text, "name": titles[n].text}
#     for n in range(len(date))
# }

print(events)
driver.quit()