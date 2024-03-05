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
    # Зайти на сайт 
    driver.get("http://uitestingplayground.com/dynamicid")
    # Проверка  наличие кнопки
    button = "[class*='btn-primar']"
    input = WebDriverWait(driver, 4).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, button))
    )
    # Кликните на синюю кнопку.
    clickable = driver.find_element(By.CSS_SELECTOR, "[class*='btn-primar']")
    actions = ActionChains(driver)
    actions.click(clickable)
    actions.perform()
    sleep(1)
    # Закрыть браузер
    driver.quit()