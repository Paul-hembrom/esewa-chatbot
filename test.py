from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
import random
import os
import json
from PIL  import Image
from io import BytesIO
import requests


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
driver.get("https://esewa.com.np/#/products/TV%20Payment/33")

# Wait for elements to load
wait = WebDriverWait(driver, 10)


# Extract name
names = [elem.text for elem in driver.find_elements("xpath", "//li[@class='ng-scope']//h5")]

# Extract image URL
image_urls = [elem.get_attribute("src") for elem in driver.find_elements("xpath", "//li[@class='ng-scope']//img")]

# Create a folder to save images
os.makedirs("downloaded_images", exist_ok=True)

# List to store name-image mapping
data = []

# Download and save images
for name, img_url in zip(names, image_urls):
    try:
        response = requests.get(img_url)
        if response.status_code == 200:
            # Open image from bytes
            img = Image.open(BytesIO(response.content))
            # Define the filename (sanitize name to avoid invalid characters)
            safe_name = name.replace(" ", "_").replace("/", "_")
            filename = f"downloaded_images/{safe_name}.jpg"
            img.save(filename, format="JPEG")
            print(f"Saved: {filename}")

            # Append data to list
            data.append({"name": name, "image_path": filename})
        else:
            print(f"Failed to download {img_url}")
    except Exception as e:
        print(f"Error downloading {img_url}: {e}")

# Save data to a JSON file
with open("name_image_mapping.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print("Data saved in name_image_mapping.json")

# Close the driver
driver.quit()