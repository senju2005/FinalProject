from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.reddit.com/login/")

try:
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/shreddit-app/shreddit-overlay-display/div[5]/input"))
    )
    username.send_keys("nihat.rzayev1357@gmail.com") 

    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/shreddit-app/shreddit-overlay-display/div[6]/input"))
    )
    password.send_keys("salam1234salam")

    password.send_keys(Keys.RETURN)

    time.sleep(5)
finally:
    driver.quit()
