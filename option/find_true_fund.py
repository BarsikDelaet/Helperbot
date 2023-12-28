import requests
from bs4 import BeautifulSoup


def find_fund(name_fond):
    """ Поиск фондов и организаций"""
    results = []
    name_fond_plus = '+'.join(name_fond.split())
    response = requests.get(f'https://dobro.mail.ru/sos/?query={name_fond_plus}')
    contents = response.text
    bs = BeautifulSoup(contents, 'lxml')
    address = bs.find_all('h2', '_0723666f2f vkuiTitle vkuiTitle--level-2')

    for name in address:
        results.append(name.text.islower())

    if name_fond.islower() in results:
        return True
    else:
        return False
