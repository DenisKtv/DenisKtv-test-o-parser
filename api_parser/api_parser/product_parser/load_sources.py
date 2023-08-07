from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
import time


class UseSelenium:
    def __init__(self, url: str, filename: str):
        self.url = url
        self.filename = filename

    def save_page(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64;"
                             "x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/114.0.5735.90 Safari/537.3")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless")

        s = Service(
            executable_path="api_parser/product_parser/lib/chromedriver"
        )

        driver = webdriver.Chrome(service=s, options=options)

        try:
            driver.get(self.url)
            time.sleep(3)
            driver.execute_script("window.scrollTo(5,4000);")
            time.sleep(5)
            html = driver.page_source
            with open(
                'api_parser/product_parser/pages/' + self.filename,
                'w',
                encoding='utf-8'
            ) as f:
                f.write(html)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()


def download_pages():
    url = "https://ozon.by/seller/proffi-1/products/?miniapp=seller_1"

    # Ограничим парсинг первыми 2 страницами
    MAX_PAGE = 2
    i = 1
    while i <= MAX_PAGE:
        filename = 'page_' + str(i) + '.html'
        if i == 1:
            UseSelenium(url, filename).save_page()
        else:
            url_param = url + '?page=' + str(i)
            UseSelenium(url_param, filename).save_page()

        i += 1


if __name__ == '__main__':
    download_pages()
