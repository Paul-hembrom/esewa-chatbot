from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

chromedriver_path = "C:\\Users\\demot\\venv\\Lib\\site-packages\\chromedriver_py\\chromedriver_win64.exe"
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument(f"user-agent={random.choice([
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
])}")

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# page url
driver.get("https://esewa.com.np/#/home")

# Wait for elements to load
wait = WebDriverWait(driver, 10)

# Extracting menu details
menu_title = driver.find_element("xpath", "//li[@class='menu-item sidebar-menu-item paymentMenu-dropdown  ng-scope']/a").text
menu_link = driver.find_element("xpath", "//li[@class='menu-item sidebar-menu-item paymentMenu-dropdown  ng-scope']/a").get_attribute("href")

print(f"Menu Title: {menu_title}")
print(f"Menu Link: {menu_link}")

driver.quit()