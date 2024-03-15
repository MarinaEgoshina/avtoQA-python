from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

# Зайти на сайт 
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Дождитесь загрузки всех картинок.
images = WebDriverWait(driver, 20).until_not(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#spinner"))
)

# Получите значение атрибута src у 3-й картинки.
src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")
print(src)
