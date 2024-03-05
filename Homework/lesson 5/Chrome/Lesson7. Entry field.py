from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Зайти на сайт 
driver.get("http://the-internet.herokuapp.com/inputs")

# Ожидать появления поля ввода
input_locator = "input[type='number']"
input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, input_locator))
)

# Введите в поле текст `1000`.
input_locator = "input[type='number']"
input = driver.find_element(By.CSS_SELECTOR, input_locator)
input.send_keys("1000")

sleep(2)

# Очистите это поле (метод `clear`).
input_locator = "input[type='number']"
input = driver.find_element(By.CSS_SELECTOR, input_locator).clear()

sleep(2)

# Введите в это же поле текст `999`.
input_locator = "input[type='number']"
input = driver.find_element(By.CSS_SELECTOR, input_locator)
input.send_keys("999")

sleep(2)