import glob

from bs4 import BeautifulSoup


def get_pages() -> list:
    return glob.glob('api_parser/product_parser/pages/*.html')


def get_html(page: str):
    with open(page, 'r', encoding='utf-8') as f:
        return f.read()


def parse_data(html: str) -> list:
    soup = BeautifulSoup(html, 'html.parser')

    links = []
    # Класс меняется с каким-то интервалом
    products_elements = soup.find_all('div', attrs={'class': 'io3 o3i'})

    for element in products_elements:
        products = element.find_all('a')
        for product in products:
            link = product.get('href').split('?')[0]
            if link not in links:
                links.append(link)

    return links


def parse_links_from_pages(products_count):
    pages = get_pages()

    all_links = []
    counter = 0

    for page in pages:
        html = get_html(page)
        links = parse_data(html)

        for link in links:
            if counter >= products_count:
                break
            all_links.append(link)
            counter += 1

        if counter >= products_count:
            break

    with open(
        'api_parser/product_parser/product_links.txt',
        'w',
        encoding='utf-8'
    ) as f:
        for link in all_links:
            f.write(link + '\n')
