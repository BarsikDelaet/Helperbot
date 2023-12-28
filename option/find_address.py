import requests
from bs4 import BeautifulSoup


def find_in_city(city, items):
    """ Поиск адресов в городе """
    result = []

    response = requests.get(f'https://yandex.ru/maps/10945/uhta/search/пункт%20примёма%20{items}%20в%20городе%20{city}')
    contents = response.text
    bs = BeautifulSoup(contents, 'lxml')
    address = bs.find_all('a', 'search-business-snippet-view__address')

    for name in address:
        result.append(name.text)

    return result
