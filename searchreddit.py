from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ChromeDriver ilə brauzeri işə salırıq
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.reddit.com/login/")

try:
    # Username sahəsini gözləyirik və məlumat daxil edirik
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/shreddit-app/shreddit-overlay-display/div[5]/input"))
    )
    username.send_keys("nihat.rzayev1357@gmail.com")  # İstifadəçi adını daxil edin

    # Password sahəsini gözləyirik və məlumat daxil edirik
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/shreddit-app/shreddit-overlay-display/div[6]/input"))
    )
    password.send_keys("salam1234salam")  # Parolu daxil edin

    # Girişi təsdiqləmək üçün Enter düyməsinə basırıq
    password.send_keys(Keys.RETURN)

    # Girişdən sonra bir neçə test həyata keçirək
    try:
        # 1. Səhifənin başlığını yoxlayın
        assert "Reddit" in driver.title
        
        # 2. Axtarış sahəsini gözləyirik və "quality assurance" yazırıq
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/shreddit-app/reddit-header-large/reddit-header-action-items/header/nav/div[2]/div/div/search-dynamic-id-cache-controller/reddit-search-large//div/div[1]/form/faceplate-search-input//label/div/span[2]/input"))  # Axtarış sahəsinin XPath-ı
        )
        #search_box.click()
        search_box.send_keys("quality assurance")  # Axtarış sözü daxil edilir

        # Axtarış düyməsini basırıq
        search_box.send_keys(Keys.RETURN)  # Enter düyməsi ilə axtarışı təsdiqləyirik

        # Axtarış nəticələrinin yüklənməsini gözləyirik
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'quality assurance')]"))  # Axtarış nəticələrinin XPath-ı
        )
        print("Axtarış nəticələri uğurla yükləndi.")

        # 3. İstifadəçi profilinin görünməsini yoxlayın
        user_profile_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/shreddit-app/reddit-header-large/reddit-header-action-items/header/nav/div[3]/div[2]/shreddit-async-loader/faceplate-dropdown-menu/faceplate-tooltip/button"))  # Profil ikonunun XPath-ı
        )
        user_profile_icon.click()  # Profil ikonuna klikləyirik
        
        # 4. Çıxış düyməsini tapın və basın
        logout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/shreddit-app/reddit-header-large/reddit-header-action-items/header/nav/div[3]/div[2]/shreddit-async-loader/faceplate-dropdown-menu/div/ul[1]/faceplate-tracker[5]/li/div"))
        )
        logout_button.click()  # Çıxış düyməsinə klikləyirik
        
        # 5. Çıxışdan sonra giriş səhifəsinin yükləndiyini yoxlayın
        assert "login" in driver.current_url
        print("Testlər müvəffəqiyyətlə tamamlandı.")

    except Exception as e:
        print(f"Test zamanı xəta baş verdi: {e}")

    time.sleep(5)  # Nəticələri görmək üçün qısa fasilə

finally:
    # Brauzeri bağlayırıq
    driver.quit()
