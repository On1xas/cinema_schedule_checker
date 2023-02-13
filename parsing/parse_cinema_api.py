import requests
from lxml import etree
import xml.etree.ElementTree as ET
from config.config import parsing_url_api
import datetime


theatre = input('Введите номер кинотера:\nArena - 2\nDana - 3\nPalazzo - 19\nTRINITI - 11\n')


def parse_schedule_api(theater: str) -> None:
    '''
    Функция делает API запрос с атрибутом "showtimes", получает в ответ html\text от сервера в формате xml с данными сеансов кинотеатра

    :param theater:
    Обозначает номер кинотеатра:
                                    Arena - 2
                                    Dana - 3
                                    Palazzo - 19
                                    TRINITI - 11
    :return: Функция возврашает None, создает/редактирует schedule.txt в корне проекта для дальнейшего парсинка сеансов кинотеатра
    '''
    date = datetime.datetime.now()
    url = f'{parsing_url_api}{date.date()}&theater={theater}'
    request = requests.get(url)
    with open('schedule_api.txt', 'w', encoding='utf-8') as w:
        w.write(request.text)


parse_schedule_api(theatre)

with open('schedule_api.txt', 'r', encoding='utf-8') as r:
    xml = r.read()
parser = etree.XMLParser(recover=True)
root = ET.fromstring(xml, parser=parser)
for i in range(1, len(root[0])):
    print(f'{root[0][i][29].text}, {root[0][i][28].text}, {root[0][i][2].text}, {root[0][i][15].text}, {root[0][i][34].text}')

    # print(f'ShowID - {root[0][i][0].text}\nStartTimeShow - {root[0][i][2].text}\nShowTitle - {root[0][i][15].text}\nEventID - {root[0][i][14].text}\nEventID - {root[0][i][14].text}\nRating - {root[0][i][21].text}\nRoom - {root[0][i][28].text}\nTheatre - {root[0][i][29].text}\nFormat - {root[0][i][34].text}\n ')


 

import datetime
import requests
import sqlite3
db_path='./parseshowdb.db'
def create_table(path):
    table=f'ShowsTheatre'

    con=sqlite3.connect(path)
    cur=con.cursor()

    query=f'CREATE TABLE IF NOT EXISTS {table} (id,Theatre,Room,StartTimeShow,ShowTitle,Rating,Format,Audio)'

    cur.execute(query)
    con.commit()
    con.close()

create_table(db_path)
           
'''
