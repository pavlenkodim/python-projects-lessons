from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time # для остановки времени

# Имитируем телефон
mobile_emulation = {"deviceName": "iPhone X"}
# Опции для браузера
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

# Получили input со страницы по атрибуту name
text_box = driver.find_element(by=By.NAME, value="my-text")
# Нашли кнопку по селектору
submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn.btn-outline-primary.mt-3")
comment_fild = driver.find_element(by=By.TAG_NAME, value="textarea")
link_to_index = driver.find_element(by=By.XPATH, value="//a")

# Обновить страницу
driver.refresh()
# Отчистить поле ввода
text_box.clear()

# Drag and Drop действия
element = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
# element - чтонужно перетащить
# target - цель, куда нужно перетащить
ActionChains(driver).drag_and_drop(element, target).perform()

# Получаем нескольколько элементов
labels = driver.find_elements(by=By.TAG_NAME, value="label")
# Обрабатываем их в цикле
for label in labels:
    print(label.text)

# Напечатали текст в input
text_box.send_keys("Selenium")
# Нажали на кнопку (имитация клик мыши)
submit_button.click()

# Получили ответ со страницы
message = driver.find_element(by=By.ID, value="message")
# Ответ в нашем коде можем использовать как нам захочется
text = message.text

input("Press Enter to exit...")

driver.quit()
