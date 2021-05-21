from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    opts = Options()
    opts.add_argument('--headless')
    web = Chrome(options=opts)
    web.maximize_window()
    web.get('https://www.baidu.com')
    print(web.title)
    print(web.current_url)
    kw = web.find_element_by_xpath('//*[@id="kw"]')
    key = 'python'
    kw.send_keys(key)
    kw.submit()
    first_x = '//*[@id="container"]/div[2]/div/div[2]/span'

    wWait(web, 10, 0.2).until(ec.title_contains(key))
    first = web.find_element_by_xpath(first_x)
    print(first.text)
    web.quit()
