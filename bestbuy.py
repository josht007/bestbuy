from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

query = input("What product do you want to search for? ")

driver = webdriver.Chrome()
driver.get("https://www.bestbuy.ca")
time.sleep(3)
search = driver.find_element(By.NAME, "search")
search.send_keys(query)
search.send_keys(Keys.RETURN)
time.sleep(5)
driver.quit()
