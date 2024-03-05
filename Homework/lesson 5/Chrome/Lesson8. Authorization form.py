from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()

# Зайти на сайт 
driver.get("http://the-internet.herokuapp.com/login")

# Ожидать появления поля ввода
try:
    usernameLocator = "#username"
    passwordLocator = "#password"
    inputUsername = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, usernameLocator))
    )
    inputPassword = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, passwordLocator))
    )
except NoSuchElementException:
        print("Ошибка отображения")
        sleep(1)


# В поле username введите значение `tomsmith`.
inputUsername.send_keys("tomsmith")

sleep(2)

# В поле password введите значение `SuperSecretPassword!`.
inputPassword.send_keys("SuperSecretPassword!")

sleep(2)

# Нажмите кнопку `Login`.
clickable = driver.find_element(By.CSS_SELECTOR, "button.radius")
actions = ActionChains(driver)
actions.click(clickable)
actions.perform()

# Проверка на успешную регистрацию 
successLog = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class*='success']"))
    )
sleep(2)

