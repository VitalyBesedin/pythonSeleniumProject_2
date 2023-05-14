from selenium import webdriver
from selenium.webdriver.common.by import By
import time

base_url = "https://www.degreesymbol.net/"

try:
    browser = webdriver.Chrome()
    browser.get(base_url)

    # input1 = browser.find_element(By.TAG_NAME, 'div:first-child > input')
    # input1 = browser.find_element(By.TAG_NAME, 'input')
    # input1.send_keys("Ivan")
    # input2 = browser.find_element(By.NAME, 'last_name')
    # input2.send_keys("Petrov")
    # input3 = browser.find_element(By.CLASS_NAME, 'city')
    # input3.send_keys("Smolensk")
    # input4 = browser.find_element(By.ID, "country")
    # input4.send_keys("Russia")
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()
    link = browser.find_element(By.LINK_TEXT, 'Degree Symbol in Math')
    link.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
