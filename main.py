from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Open the browser
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# Step 2: Open the website
driver.get("https://www.chatgpt.com")

# Step 3: Wait for the page to load
time.sleep(5)  # Adjust if needed based on your connection speed

# Step 4: Find the element by its class
try:
    element = driver.find_element(By.CSS_SELECTOR, "div.px-1.text-pretty.whitespace-pre-wrap")
    print("Extracted text:", element.text)
except Exception as e:
    print("Element not found:", e)

# Step 5: Close the browser
driver.quit()
