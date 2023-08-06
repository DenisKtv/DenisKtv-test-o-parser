from bs4 import BeautifulSoup
import glob


def get_pages() -> list:
    return glob.glob('parser/pages/*.html')


def get_html(page: str):
    with open(page, 'r', encoding='utf-8') as f:
        return f.read()


def parse_data(html: str) -> list:
    soup = BeautifulSoup(html, 'html.parser')

    links = []
    products_elements = soup.find_all('div', attrs={'class': 'i9j ik'})

    for element in products_elements:
        products = element.find_all('a')
        for product in products:
            link = product.get('href').split('?')[0]
            if link not in links:
                links.append(link)

    return links


def main():
    pages = get_pages()

    all_links = []

    for page in pages:
        html = get_html(page)
        links = parse_data(html)
        all_links.extend(links)

    with open('parser/product_links.txt', 'w', encoding='utf-8') as f:
        for link in all_links:
            f.write(link + '\n')


if __name__ == '__main__':
    main()
