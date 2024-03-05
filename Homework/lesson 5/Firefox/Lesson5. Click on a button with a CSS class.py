from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.
iterations = 3
for _ in range(iterations):
    driver = webdriver.Firefox()
    driver.maximize_window()
    # Откройте страницу
    driver.get("http://uitestingplayground.com/classattr")
    # Проверка  наличие кнопки
    button = "//button[contains(@class,'btn-primary')]"
    input = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, button))
    )
    # Кликните на синюю кнопку.
    clickable = driver.find_element(By.XPATH, "//button[contains(@class,'btn-primary')]")
    actions = ActionChains(driver)
    actions.click(clickable)
    actions.perform()
    sleep(2)
    # Закрыть браузер
    driver.quit()