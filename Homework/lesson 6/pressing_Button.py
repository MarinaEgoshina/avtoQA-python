from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Зайти на сайт 
driver.get("http://uitestingplayground.com/ajax")
driver.implicitly_wait(20)

# Нажать на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "[id*='Button']").click()

# найти элемент - зеленая плашка. Напечатать текст 
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(txt)





