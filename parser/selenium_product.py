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
                'parser/products/' + self.filename, 'w', encoding='utf-8'
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
