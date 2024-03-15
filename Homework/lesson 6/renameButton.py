from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

# Зайти на сайт 
driver.get("http://uitestingplayground.com/textinput")

# Укажите в поле ввода текст SkyPro.
driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

# Нажмите на синюю кнопку.
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# Получите текст кнопки и выведите в консоль (“SkyPro”).
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(button)