from celery import shared_task
from .models import Product

from api_parser.product_parser.load_sources import download_pages
from api_parser.product_parser.link_collector import parse_links_from_pages
from api_parser.product_parser.get_product_json import fetch_json_files_from_links
from api_parser.product_parser.get_product_data import parse_all_products


@shared_task
def parse_products():
    # Скачиваем страницы с продуктами
    download_pages()

    # Парсим ссылки на продукты со страниц
    parse_links_from_pages()

    # Получаем JSON данные продуктов по ссылкам
    fetch_json_files_from_links()

    # Парсим данные продуктов из JSON файлов
    products_data = parse_all_products()

    # Сохраняем данные продуктов в базу данных
    for product_data in products_data:
        product = Product(
            title=product_data['title'],
            description=product_data['description'],
            link=product_data['link'],
            price=product_data['price'],
            original_price=product_data['original_price'],
            image=product_data['cover_image'],
        )
        product.save()

    print(f"{len(products_data)} products have been saved to the database.")

    return f"{len(products_data)} products parsed and saved."
