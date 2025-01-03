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

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/shreddit-app/shreddit-overlay-display/div[5]/input"))
)
username.send_keys("nihat.rzayev1357@gmail.com")

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/shreddit-app/shreddit-overlay-display/div[6]/input"))
)
password.send_keys("salam1234salam")

password.send_keys(Keys.RETURN)

assert "Reddit" in driver.title

user_profile_icon = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/shreddit-app/reddit-header-large/reddit-header-action-items/header/nav/div[3]/div[2]/shreddit-async-loader/faceplate-dropdown-menu/faceplate-tooltip/button"))  # Profil ikonunun XPath-ı
)
user_profile_icon.click()

logout_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/shreddit-app/reddit-header-large/reddit-header-action-items/header/nav/div[3]/div[2]/shreddit-async-loader/faceplate-dropdown-menu/div/ul[1]/faceplate-tracker[5]/li/div"))
)
logout_button.click()
time.sleep(5)

driver.quit()
