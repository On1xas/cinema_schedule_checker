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

'''
            0 - <ID>180224</ID>
            1 - <dtAccounting/>
            2 - <dttmShowStart>2023-1-21T11:15:00</dttmShowStart>
            3 - <dttmShowStartUTC/>
            4 - <dttmShowEnd/>
            5 - <dttmShowEndUTC/>
            6 - <ShowSalesStartTime/>
            7 - <ShowSalesStartTimeUTC/>
            8 - <ShowSalesEndTime/>
            9 - <ShowSalesEndTimeUTC/>
           10 - <ShowReservationStartTime/>
           11 - <ShowReservationStartTimeUTC/>
           12 - <ShowReservationEndTime/>
           13 - <ShowReservationEndTimeUTC/>
           14 - <EventID>2643</EventID>
           15 - <Title><![CDATA[ Кот в сапогах 2: Последнее желание ]]></Title>
           16 - <OriginalTitle><![CDATA[ Кот в сапогах 2: Последнее желание]]></OriginalTitle>
           17 - <ProductionYear>2022</ProductionYear>
           18 - <LengthInMinutes>110</LengthInMinutes>
           19 - <dtLocalRelease>2023-1-14T00:00:00</dtLocalRelease>
           20 - <Rating>зрителям, достигшим 6 лет</Rating>
           21 - <RatingLabel>6+</RatingLabel>
           22 - <RatingImageUrl/>
           23 - <EventType/>
           24 - <Genres>комедия, мультфильм, приключения</Genres>
           25 - <TheatreID>2</TheatreID>
           26 - <TheatreAuditriumID>18</TheatreAuditriumID>
           27 - <TheatreAuditriumURL/>
           28 - <TheatreAuditorium>Зал 4</TheatreAuditorium>
           29 - <Theatre>Silver Screen в ТРЦ Arena city</Theatre>
           30 - <TheatreAndAuditorium>Silver Screen в ТРЦ Arena city, Зал 4</TheatreAndAuditorium>
           31 - <PresentationMethodAndLanguage/>
           32 - <EventSeries/>
           33 - <ShowURL>https://silverscreen.by/afisha/#times=kot-v-sapogah-2-poslednee-zhelanie-2643&showID=180224</ShowURL>
           34 - <PresentationMethod>2D</PresentationMethod>
           35 - <EventURL>https://silverscreen.by/afisha/kot-v-sapogah-2-poslednee-zhelanie-2643</EventURL>
           36 - <Images>
                <EventMicroImagePortrait/>
                <EventSmallImagePortrait/>
                <EventMediumImagePortrait/>
                <EventLargeImagePortrait>https://portal.silverscreen.by:8448/meadiaStorage/bin/system/cinema/eventsphoto/medium/10016.jpeg</EventLargeImagePortrait>
                </Images>
           37 - <ContentDescriptors/>
           38 - <hav_tickets>true</hav_tickets>
           39 - <min_price>7</min_price>
           40 - <max_price>32</max_price>
 

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
