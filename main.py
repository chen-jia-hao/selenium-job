from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    opts = Options()
    opts.add_argument('--headless')
    web = Chrome(options=opts)
    web.maximize_window()
    web.get('https://www.baidu.com')
    print(web.title)
    print(web.current_url)
    print(web.session_id)
    web.quit()
