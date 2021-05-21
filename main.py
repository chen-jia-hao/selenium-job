from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    opts = Options()
    opts.add_argument('--headless')
    web = Chrome(options=opts)
    web.get('https://www.baidu.com')
    print(web.title)
    web.quit()
