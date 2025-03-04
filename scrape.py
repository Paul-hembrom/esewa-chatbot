import json
import random
import time
import logging
import requests
import base64  # Added missing import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

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
driver.get("https://esewa.com.np/#/products/Education%20Payment/1")

# Wait for elements to load
wait = WebDriverWait(driver, 120)

# Wait until the list of names is visible
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@class='ng-scope']//h5")))

# Extract all names
names =[elem.text for elem in driver.find_elements("xpath", "//li[@class='ng-scope']//h5")]

# Save names in a JSON file
with open("Education Payment.json", "w", encoding="utf-8") as json_file:
    json.dump(names, json_file, indent=4, ensure_ascii=False)

print("Names saved in names.json")

# Close the driver
driver.quit()