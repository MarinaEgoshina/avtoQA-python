from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()

# Откройте страницу 
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Ожидать появления модального окна
modal_locator = "//div[@style='display: block;']"
input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, modal_locator))
)
sleep(2)

# Ожидание кликабельности кнопки Close
close_button_locator = "//*[contains(text(), 'Close')]"
close_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, close_button_locator))
)
# Нажмите кнопку Close
actions = ActionChains(driver)
close_button.click()
actions.perform()

# Ожидаем исчезновения модального окна
modal_close = "//div[@style='display: none;']"
WebDriverWait(driver, 5).until_not(EC.visibility_of_element_located((By.XPATH, modal_close)))
sleep(2)

# Закрыть браузер
driver.quit()
