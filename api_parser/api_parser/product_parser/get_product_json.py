import random
import ssl
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

ssl._create_default_https_context = ssl._create_unverified_context


class UseSelenium:
    def __init__(self, url: str, filename: str):
        self.url = url
        self.filename = filename

    def save_page(self):
        persona = self.__get_headers_proxy()

        options = uc.ChromeOptions()
        options.add_argument(f"user-agent={persona['user-agent']}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless")
        options.add_argument('--disable-gpu')  # Если используется Windows

        driver = uc.Chrome(options=options)

        try:
            driver.get(self.url)
            elem = driver.find_element(By.TAG_NAME, "pre").get_attribute(
                'innerHTML'
            )
            with open(
                'api_parser/product_parser/products/' + self.filename,
                'w',
                encoding='utf-8'
            ) as f:
                f.write(elem)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()

    def __get_headers_proxy(self) -> dict:
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/114.0.5735.90 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.90 '
            'Safari/537.36',
        ]
        return {
            'user-agent': random.choice(user_agents),
        }


def get_product_links() -> list:
    with open(
        'api_parser/product_parser/product_links.txt',
        'r',
        encoding='utf-8'
    ) as f:
        return f.readlines()


def data_parsing(product: str, i: int, filename: str) -> None:
    url = 'https://www.ozon.by/api/composer-api.bx/page/json/v2' \
          f'?url={product}'

    filename = filename + str(i) + '.html'
    print(f"Processing URL: {url}")
    UseSelenium(url, filename).save_page()


def fetch_json_files_from_links(products_count=10):
    products = get_product_links()
    products_count = min(products_count, 50)

    for i, product in enumerate(products[:products_count], start=1):
        data_parsing(product, i, filename='')
