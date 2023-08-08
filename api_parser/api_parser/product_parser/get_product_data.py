import json
import glob


def get_json(filename: str) -> dict:
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        return json.loads(data)


def get_info_from_json(json_data: dict) -> tuple:
    widget_states = json_data.get('widgetStates')

    title, price, original_price, cover_image = None, None, None, None

    for key in widget_states:
        if key.startswith('webProductHeading'):
            web_product_heading = json.loads(widget_states[key])
            title = web_product_heading.get('title')

        if key.startswith('webPrice-'):
            web_price = json.loads(widget_states[key])
            price = web_price.get('price')
            original_price = web_price.get('originalPrice')

        if key.startswith('webGallery-'):
            web_gallery = json.loads(widget_states[key])
            cover_image = web_gallery.get('coverImage')

    return title, price, original_price, cover_image


def get_description_from_json(json_data: dict) -> tuple:
    try:
        seo_data = json_data.get('seo', {})
        script_data = seo_data.get('script', [])
        description = None
        for script in script_data:
            if 'innerHTML' in script:
                inner_html = script['innerHTML']
                inner_json = json.loads(inner_html)
                if 'description' in inner_json:
                    description = inner_json['description']

        link_data = seo_data.get('link', [])
        href = None
        if link_data:
            href = link_data[0].get('href')

        return description, href

    except Exception as e:
        print(f'Error occurred: {str(e)}')
        return None, None


def parse_all_products(products_count=None):
    products = []
    filenames = sorted(
        glob.glob('api_parser/product_parser/products/*.html'),
        key=lambda name: int(name.split('/')[-1].split('.')[0])
    )

    if products_count:
        filenames = filenames[:products_count]

    for filename in filenames:
        print(f"Processing file: {filename}")
        data = get_json(filename)
        description, link = get_description_from_json(data)
        title, price, original_price, cover_image = get_info_from_json(data)
        product = {
            'title': title,
            'description': description,
            'link': link,
            'price': price,
            'original_price': original_price,
            'cover_image': cover_image
        }
        products.append(product)

    print(products)
    return products
