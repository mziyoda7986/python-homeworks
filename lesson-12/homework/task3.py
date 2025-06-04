from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

driver = webdriver.Chrome()

driver.get('https://www.demoblaze.com')
time.sleep(3)

laptops_link = driver.find_element(By.LINK_TEXT, 'Laptops')
laptops_link.click()
time.sleep(3)

def scrape_current_page():
    laptops = []
    cards = driver.find_elements(By.CLASS_NAME, 'card-block')
    for card in cards:
        name = card.find_element(By.TAG_NAME, 'a').text
        price = card.find_element(By.TAG_NAME, 'h5').text
        description = card.find_element(By.TAG_NAME, 'p').text
        laptops.append({
            'name' : name,
            'price': price,
            'description' : description
        })
    return laptops

laptops = scrape_current_page()

next_button = driver.find_element(By.ID, 'next2')
next_button.click()
time.sleep(3)

laptops += scrape_current_page()

with open('laptops.json', mode='w', encoding='utf-8') as file:
    json.dump(laptops, file, indent=2)

driver.quit()