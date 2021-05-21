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
    kw.send_keys('python')
    kw.submit()

    first_x = '//*[@id="content_left"]/div/div/h3/a'

    # wWait(web, 10, 0.2).until(ec.presence_of_element_located((By.XPATH, first_x)))
    time.sleep(10)
    first = web.find_element_by_xpath(first_x)
    print(first.text)
    web.quit()
