import sqlite3
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
        'Введите дату которую хотите проверить в формате 2023-01-01(YYYY-MM-DD). Если хотите проверить сегодняшний день, ничего не вводите\n')

    if dates == "":
        dates = datetime.datetime.now().date()
    if theatre == "":
        url = f'{parsing_url_api}{dates}'
    else:
        url = f'{parsing_url_api}{dates}&theater={theatre}'
    print(f"{parse_schedule_api.__name__}***Выполняю запрос сеансов из программного обеспечения кинотеатра***")
    request = requests.get(url)
    # with open('schedule_api.txt', 'w', encoding='utf-8') as w:
    #     w.write(request.text)
    # with open('schedule_api.txt', 'r', encoding='utf-8') as r:
    if request.status_code == 200:
        print(f'{parse_schedule_api.__name__}***Ответ получен успешно***')
        xml = request.text
        parser = etree.XMLParser(recover=True)
        root = ET.fromstring(xml, parser=parser)
        for i in range(1, len(root[0])):
            data_parsing_api.append(
                (
                    root[0][i][29].text, root[0][i][28].text, root[0][i][2].text, root[0][i][15].text,
                    root[0][i][34].text))
        return list(sorted(data_parsing_api, key=lambda x: x[2]))
    else:
        print(
            f'{parse_schedule_api.__name__}***Проверьте полученные данные, возможно запрос был выполнен некорректно или не выполнен вовсе. Ошибка запроса {request.status_code}.***')
        return None


def insert_data_api_sql(show):
    theatre = show[0]
    room = show[1]
    if theatre == 'mooon в ТРК Triniti':
        theatre = 'TRINITI'
        if room == 'Зал 1':
            return f"INSERT INTO TRINITI_1_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 2 Lounge':
            return f"INSERT INTO TRINITI_2_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 3 Premiere':
            return f"INSERT INTO TRINITI_3_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 4 Resto':
            return f"INSERT INTO TRINITI_4_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 5 VIP':
            return f"INSERT INTO TRINITI_5_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
    if theatre == 'mooon в ТРЦ Dana Mall':
        theatre = 'DANA'
        if room == 'Зал 1 Premiere':
            return f"INSERT INTO DANA_1_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 2':
            return f"INSERT INTO DANA_2_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 3 Screen X':
            return f"INSERT INTO DANA_3_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 4 Vegas lounge':
            return f"INSERT INTO DANA_4_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 5':
            return f"INSERT INTO DANA_5_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 6 VIP':
            return f"INSERT INTO DANA_6_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 7 VIP':
            return f"INSERT INTO DANA_7_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"

    if theatre == 'mooon в ТРЦ Palazzo':
        theatre = 'PALAZZO'
        if room == 'Зал 1 mooon IMAX':
            return f"INSERT INTO PALAZZO_1_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 2 Vegas':
            return f"INSERT INTO PALAZZO_2_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 3 VIP':
            return f"INSERT INTO PALAZZO_3_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 4 Resto':
            return f"INSERT INTO PALAZZO_4_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 5 mooon+  ':
            return f"INSERT INTO PALAZZO_5_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 6 Kids':
            return f"INSERT INTO PALAZZO_6_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 7 Visa Premiere':
            return f"INSERT INTO PALAZZO_7_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
    if theatre == 'Silver Screen в ТРЦ Arena city':
        theatre = 'ARENA'
        if room == 'Зал 1':
            return f"INSERT INTO ARENA_1_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 2':
            return f"INSERT INTO ARENA_2_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 3':
            return f"INSERT INTO ARENA_3_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 4':
            return f"INSERT INTO ARENA_4_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 5':
            return f"INSERT INTO ARENA_5_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 6':
            return f"INSERT INTO ARENA_6_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"


set_show=set()
connect = sqlite3.connect('..\data\database.db')
cur = connect.cursor()
for show in parse_schedule_api():
    set_show.add(show[3])
    cur.execute(insert_data_api_sql(show), show)
    connect.commit()
for show in set_show:
    cur.execute(f'INSERT INTO PIVOT_SHOW_TABLE (SHOW_NAME_API, LAST_UPDATE) VALUES(?,?)', (show, datetime.datetime.now()))
    connect.commit()
connect.close()
print(set_show)