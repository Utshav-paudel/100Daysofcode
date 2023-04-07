from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = r"C:\Users\utsha\OneDrive\Desktop\chrome driver\chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
# automating task below here
driver.get("https://en.wikipedia.org/wiki/Main_Page")
number_of_articles = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
print(number_of_articles.text)