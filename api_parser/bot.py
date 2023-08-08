import os
import django
from dotenv import load_dotenv
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater, CommandHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_parser.settings')
django.setup()

from products.models import Product, ParserConfiguration

load_dotenv()


def start(update, context):
    update.message.reply_text('Привет! Я ваш бот.')


def products(update, context):
    parser_config = ParserConfiguration.objects.latest('pub_date')
    products_count = parser_config.products_count
    products_list = Product.objects.all().order_by('-id')[:products_count]
    text = 'Список последних товаров:\n'
    for idx, product in enumerate(products_list, start=1):
        text += f"{product.id}: {product.title} - {product.link}\n"
    update.message.reply_text(text)


def message_handler(update, context):
    text = update.message.text.lower()
    if text == 'список товаров':
        products(update, context)


def main():
    token = os.getenv('ADMIN_TOKEN')
    updater = Updater(token,)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(
        MessageHandler(Filters.text & ~Filters.command, message_handler)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
