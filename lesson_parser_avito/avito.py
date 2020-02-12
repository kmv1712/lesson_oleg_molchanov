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
    soup = BeautifulSoup(html, 'lxml')
    
    pages = soup.find('div', class='pagination-pages')


def main():
    # https://www.avito.ru/yaroslavl
    # https://www.avito.ru/yaroslavl/mebel_i_interer/krovati_divany_i_kresla?q=%D0%B4%D0%B8%D0%B2%D0%B0%D0%BD
    pass



if __name__ == '__main__':
    main()
