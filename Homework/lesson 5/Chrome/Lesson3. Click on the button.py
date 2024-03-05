from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Зайти на сайт 
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Проверка  наличие кнопки Add Element
addElement = "button[onclick='addElement()']"
input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, addElement))
)

# Пять раз кликните на кнопку Add Element
clickable = driver.find_element(By.CSS_SELECTOR, addElement)
actions = ActionChains(driver)
for _ in range(5):
    actions.click(clickable)
actions.perform()

# Соберите со страницы список кнопок Delete
buttonDeletes = driver.find_elements(By.CSS_SELECTOR, "button[onclick='deleteElement()']")
print("Колличество кнопок Delete:", len(buttonDeletes))

sleep(1)