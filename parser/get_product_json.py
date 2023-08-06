from selenium_product import UseSelenium


def get_product_links() -> list:
    with open('parser/product_links.txt', 'r', encoding='utf-8') as f:
        return f.readlines()


def data_parsing(product: str, i: int, filename: str) -> None:
    url = 'https://www.ozon.by/api/composer-api.bx/page/json/v2' \
          f'?url={product}'

    filename = filename + str(i) + '.html'
    print(f"Processing URL: {url}")
    UseSelenium(url, filename).save_page()


def main():
    products = get_product_links()
    i = 1
    for product in products:
        if i < 3:
            data_parsing(product, i, filename='')
            i += 1
        else:
            break


if __name__ == '__main__':
    main()
