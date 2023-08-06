import json
import glob


def get_json(filename: str) -> dict:
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        return json.loads(data)


def get_info_from_json(json_data: dict) -> tuple:
    widget_states = json_data.get('widgetStates')

    title, price, original_price, cover_image = None, None, None, None
    # Проходимся по всем ключам в widgetStates
    for key in widget_states:
        if key.startswith('webProductHeading'):
            # Извлекаем значение ключа и загружаем его как JSON
            web_product_heading = json.loads(widget_states[key])

            # Извлекаем и возвращаем title
            title = web_product_heading.get('title')

        if key.startswith('webPrice-'):
            # Извлекаем значение ключа и загружаем его как JSON
            web_price = json.loads(widget_states[key])

            # Извлекаем и возвращаем price и originalPrice
            price = web_price.get('price')
            original_price = web_price.get('originalPrice')

        if key.startswith('webGallery-'):
            # Извлекаем значение ключа и загружаем его как JSON
            web_gallery = json.loads(widget_states[key])

            # Извлекаем и возвращаем coverImage
            cover_image = web_gallery.get('coverImage')

    if title is None:
        print("Title not found.")
    if price is None:
        print("Price not found.")
    if original_price is None:
        print("Original price not found.")
    if cover_image is None:
        print("Cover image not found.")

    return title, price, original_price, cover_image


def get_description_from_json(json_data: dict) -> tuple:
    try:
        # получаем данные из ключа 'seo'
        seo_data = json_data.get('seo', {})

        # Извлекаем описание
        script_data = seo_data.get('script', [])
        description = None
        # проходим по всем элементам в script_data
        for script in script_data:
            if 'innerHTML' in script:
                inner_html = script['innerHTML']
                inner_json = json.loads(inner_html)

                # если внутри есть ключ 'description', возвращаем его значение
                if 'description' in inner_json:
                    description = inner_json['description']

        # Извлекаем ссылку
        link_data = seo_data.get('link', [])
        href = None
        if link_data:  # Если список не пуст
            href = link_data[0].get('href')  # Извлекаем из первого элемента

        if description is None:
            print("Description not found.")
        if href is None:
            print("Link not found.")

        return description, href

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None, None


# получаем список всех html файлов в текущей директории
filenames = sorted(glob.glob("parser/products/*.html"), key=lambda name: int(
    name.split('/')[-1].split('.')[0])
)


# проходим по каждому файлу в списке
for filename in filenames:
    print(f"Processing file: {filename}")
    json_data = get_json(filename)
    title = get_description_from_json(json_data)
    description, link = get_description_from_json(json_data)
    print(f"Description: {description}")
    print(f"Link: {link}")
    title, price, original_price, cover_image = get_info_from_json(json_data)
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Original Price: {original_price}")
    print(f"Cover Image: {cover_image}")
