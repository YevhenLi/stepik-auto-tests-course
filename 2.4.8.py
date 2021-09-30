from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = 'https://suninjuly.github.io/explicit_wait2.html'

options = Options()

# открыть браузер с профилем "Profile 1"
options.add_argument("--user-data-dir=C:/Users/Yevhen/AppData/Local/Google/Chrome/User Data/")
options.add_argument('--profile-directory=Profile 1')


def calc(x):
    return str(math.log(12*math.sin(int(x))))

try:
        # запуск wevdriver chrome
    browser = webdriver.Chrome('c:/webdriver/chromedriver.exe', chrome_options=options)

    browser.get(link)

    btn = browser.find_element(By.ID, 'price')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    browser.find_element(By.ID, 'book').click()

    x = browser.find_element(By.ID, 'input_value').text
    print(f'\nx = {x}')
    y = calc(x)
    print(f'y = {y}\n')

    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.ID, 'solve').click()

    alert = browser.switch_to.alert
    alert_text = alert.text.split()[-1]
    print(f'\nCongratulation! your kode: {alert_text}')

# except Exception as err:
#     print(f'\nВозникла ошибка: {err}')


finally:
    pass
    time.sleep(5)
    browser.quit()


