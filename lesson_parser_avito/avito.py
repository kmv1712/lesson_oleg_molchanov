import requests
from bs4 import BeautifulSoup


'''
План:
    1.Выяснить количество страниц.
    2.Сформировать список урлов на страницах выдачи
    3.Собрать данные.
'''


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    """Получить количество всех страниц."""
    soup = BeautifulSoup(html, 'lxml')
    # TODO: Подумать, как получить все страницы.
    pages = soup.find('div', class_='pagination-root-2oCjZ').find_all('span', class_='pagination-item-1WyVp pagination-item_active-25YwT')[-1]
    string_with_total_pages = str(pages).split('</')[0] if str(pages).split('</') else ''
    total_pages = string_with_total_pages.split('>')[-1] if string_with_total_pages.split('>') else None
    return int(total_pages)


def get_page_data(html):
    """Получить информацию о товарах с страницы"""
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='js-catalog_serp').find_all('div', class_ = 'snippet-horizontal item item_table clearfix js-catalog-item-enum item-with-contact js-item-extended')

    # for ad in ads:


def main():
    # https://www.avito.ru/yaroslavl
    # https://www.avito.ru/yaroslavl/mebel_i_interer/krovati_divany_i_kresla?q=%D0%B4%D0%B8%D0%B2%D0%B0%D0%BD
    url = 'https://www.avito.ru/yaroslavl/mebel_i_interer/krovati_divany_i_kresla?q=%D0%B4%D0%B8%D0%B2%D0%B0%D0%BD&p=2'
    base_url = 'https://www.avito.ru/yaroslavl/mebel_i_interer/krovati_divany_i_kresla'
    page_part = '&p='
    query_part = '?q=%D0%B4%D0%B8%D0%B2%D0%B0%D0%BD'

    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages):
        url_gen = base_url = page_part + str(i) + query_part
        html = get_html(url_gen)
        get_page_data(html)


if __name__ == '__main__':
    main()
