from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = "https://www.degreesymbol.net/"

# try:
# browser = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
browser = webdriver.Chrome(options=options, service=g)
# browser = webdriver.Safari()
browser.get(url)
browser.maximize_window()

    # input1 = browser.find_element(By.TAG_NAME, 'div:first-child > input')
# link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
# link.click()
link = browser.find_element(By.PARTIAL_LINK_TEXT, 'Math')
link.click()
time.sleep(10)
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

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# не забываем оставить пустую строку в конце файла ansver: 22.343046454729887
