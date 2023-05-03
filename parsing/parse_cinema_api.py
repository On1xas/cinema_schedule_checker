import sqlite3

import requests
from lxml import etree
import xml.etree.ElementTree as ET
from config.config import parsing_url_api
import datetime
import colorama


def parse_schedule_api(dates):
    """
    Функция делает API запрос с атрибутом "showtimes",
     получает в ответ html\text от сервера в формате xml с данными сеансов кинотеатра

    :return: Функция возвращает список кортежей сеансов отсортированных по дате сеанса
    """

    data_parsing_api = []
    colorama.init()
    theatre = ''
    # input(
    # '''Введите номер кинотеара:\nArena - 2\nDana - 3\nPalazzo - 19\nTRINITI - 11\n
    # Если хотите сделать выборку по всем кинотеатрам, ничего не вводите\n''')
    # input(
    # '''Введите дату которую хотите проверить в формате 2023-01-01(YYYY-MM-DD).
    # Если хотите проверить сегодняшний день, ничего не вводите\n''')

    url = 'https://util.silverscreen.by:8448/meadiaStorage/util/schedule/list.xml'

    print(
        f"***Выполняю запрос сеансов на {colorama.Fore.RED} {dates} {colorama.Style.RESET_ALL} из программного обеспечения кинотеатра***")
    request = requests.get(url)
    if request.status_code == 200:
        print(f'***Ответ получен успешно***')

        xml = request.content.decode(encoding='utf-8')
        parser = etree.XMLParser(recover=True)
        tree = ET.fromstring(xml, parser=parser)

        for elem in range(0, len(tree[1])):
            date_time_str = tree[1][elem][1].text
            date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S')
            if dates in str(date_time_obj):
                audio_format = "EN-RU" if "(RU SUB)" in tree[1][elem][3].text else "RU-RU"

                data_parsing_api.append((tree[1][elem][14].text,
                                        tree[1][elem][13].text,
                                        tree[1][elem][1].text,
                                        tree[1][elem][3].text,
                                        tree[1][elem][16].text,
                                        audio_format))


        # for i in range(1, len(root[0])):
        #     audio_format = "EN-RU" if "(RU SUB)" in root[0][i][15].text else "RU-RU"
        #     # Добавляем в список, кортеж (Название кинотеатра, Название зала, Дата+Время сеанса, Название сеанса, Формат фильма, Аудиоформат фильма)
        #     data_parsing_api.append(
        #         (root[0][i][29].text, root[0][i][28].text, root[0][i][2].text, root[0][i][15].text,
        #              root[0][i][34].text, audio_format))
            # Возвращаем отсортированный список кортежей по дате сеанса
        return list(sorted(data_parsing_api, key=lambda x: x[2]))
    else:
        print(
            f"""***Проверьте полученные данные, возможно запрос был выполнен некорректно или не выполнен вовсе. Ошибка запроса {request.status_code}.***""")
        return None


if __name__ == '__main__':
    print(parse_schedule_api("2023-05-04"))