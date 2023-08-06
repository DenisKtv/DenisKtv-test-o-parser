from selenium_page import UseSelenium


def main():
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
    main()
