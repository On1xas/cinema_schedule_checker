from typing import List, Tuple

import requests
from lxml import etree
import xml.etree.ElementTree as ET
from config.config import parsing_url_api
import datetime


def parse_schedule_api() -> list[tuple[str | None, str | None, str | None, str | None, str | None]]:
    '''
    Функция делает API запрос с атрибутом "showtimes", получает в ответ html\text от сервера в формате xml с данными сеансов кинотеатра

    :return: Функция возвращает список кортежей сеансов
    '''

    data_parsing_api = []

    theatre = input(
        'Введите номер кинотеара:\nArena - 2\nDana - 3\nPalazzo - 19\nTRINITI - 11\nЕсли хотите сделать выборку по всем кинотеатрам, ничего не вводите\n')
    dates = input(
        'Введите дату которую хотите проверить в формате 2023-01-01. Если хотите проверить сегодняшний день, ничего не вводите\n')

    if dates == "":
        dates = datetime.datetime.now().date()
    if theatre == "":
        url = f'{parsing_url_api}{dates}'
    else:
        url = f'{parsing_url_api}{dates}&theater={theatre}'
    request = requests.get(url)
    # with open('schedule_api.txt', 'w', encoding='utf-8') as w:
    #     w.write(request.text)
    # with open('schedule_api.txt', 'r', encoding='utf-8') as r:
    xml = request.text
    parser = etree.XMLParser(recover=True)
    root = ET.fromstring(xml, parser=parser)
    for i in range(1, len(root[0])):
        data_parsing_api.append(
            (root[0][i][29].text, root[0][i][28].text, root[0][i][2].text, root[0][i][15].text, root[0][i][34].text))
    return list(sorted(data_parsing_api, key=lambda x: x[2]))
