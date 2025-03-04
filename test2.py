from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
import random
import json
import os

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
driver.get("https://esewa.com.np/#/products/Topup%20&%20Recharge/7")

time.sleep(3)  # Wait for the page to load

# Extract menu titles from the first page
menu_elements = driver.find_elements(By.CSS_SELECTOR, "li.menu-item.sidebar-menu-item a.text-ellipsis")
menus = {menu.text.strip(): menu.get_attribute("href") for menu in menu_elements}

# Create a folder to save JSON files
os.makedirs("services_json", exist_ok=True)

# Loop through each menu title and extract product names
for menu_title, menu_link in menus.items():
    driver.get(menu_link)  # Open the menu link
    time.sleep(3)  # Wait for the page to load

    # Extract product names
    product_elements = driver.find_elements(By.CSS_SELECTOR, "li.ng-scope figcaption h5")
    products = [product.text.strip() for product in product_elements]

    # Prepare JSON data
    data = {menu_title.replace(" ", ""): products}  # Removing spaces in key name

    # Save each service as a separate JSON file
    filename = f"services_json/{menu_title.replace(' ', '_')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Saved: {filename}")

# Close the driver
driver.quit()

print("\nAll services have been scraped and saved as individual JSON files.")