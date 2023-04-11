from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
cookie_counts = 0
chrome_driver_path = r"C:\Users\utsha\OneDrive\Desktop\chrome driver\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
#cookie click
cookie = driver.find_element(By.ID, "cookie")
# upgrade items
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_id = [item.get_attribute("id") for item in items]
timeout = time.time() + 5
fivemin = time.time() + 60*5 #fiveminutes
while True:
    cookie.click()
    #every 5 seconds
    if time.time() > timeout:
        #get updgrades
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        prices = []
        #changing price to int
        for price in all_prices:
            element_text = price.text
            if element_text !="":
                cost = int(price.text.replace(",","").split("-")[1].strip())
                prices.append(cost)
        #creating dictionary to store item and prices
        cookie_upgrades = {}
        for n in range(len(prices)):
            cookie_upgrades[prices[n]] = items_id[n]
        # getting current cookie count       
        cookie_count = driver.find_element(By.ID, "money").text
        if "," in cookie_count:
            cookie_count = cookie_count.replace(",", "")
        cookie_counts = int(cookie_count)
        # finding upgrades if we can afford
        affordabel_upgrades = {}
        for (cost,id) in cookie_upgrades.items():
            if cookie_counts > cost:
                affordabel_upgrades[cost] = id
        #purchase the most expensive affordable cookies
        highest_price_affordable = max(affordabel_upgrades)
        to_purchaseid = affordabel_upgrades[highest_price_affordable]
        driver.find_element(By.ID, to_purchaseid).click()
        #Adding another 5 second untill the next check
        timeout = time.time() + 5
    #stopping the bot after 5 minutes and checking cookies per second count
    if time.time() > fivemin:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
