from parsing.parse_cinema_api import *
import gspread
import time
from application.app_func import get_show_from_api
import csv
import enum

def connect_gsdb():
    gs = gspread.service_account(filename='gs_credentials.json')  # подключаем файл с ключами и пр.
    sh = gs.open_by_key('17C7Ch7S9a3vHUIW3B8wGl7b_OYk9MuBRcssG6rbAGVQ')  # подключаем таблицу по ID
    worksheet = sh.sheet1  # получаем первый лист

    print('Google Sheet - CinemaShowDB Connected')
#    print(len(worksheet.get_all_values()))
    return worksheet
def add_show_gsdb():
    worksheet= connect_gsdb()
    data=get_show_from_api("2023-03-01")
    quote=0
    with open('test.csv', 'w', newline='') as write_file:
        writer=csv.writer(write_file)
        for item in data:
            writer.writerow(item)
    with open('test.csv', 'r', newline='') as read_file:
        reader=csv.reader(read_file)
        for item in reader:
            print(item)
            if quote // 55 == 1:
                print(f"CLEAR QUOTE = {quote}. TIMEOUT 65 SEC")
                quote=0
                time.sleep(65)
                print(f"TIMEOUT END. QUOTE = {quote}")
            quote+=1
            worksheet.append_row(item)
            time.sleep(0.3)
        print(f"CLEAR QUOTE = {quote}. TIMEOUT 65 SEC")
        time.sleep(65)


def clear_gsdb():
    quote=0
    worksheet=connect_gsdb()
    print(f"CLEAR ROW IN CinemaShowDB. Detected - {len(worksheet.col_values(1))-1} SHOWS")
    time.sleep(2)
    for row in range(1, len(worksheet.col_values(1))):
        if quote // 55 == 1:
            print(f"CLEAR QUOTE = {quote}. TIMEOUT 65 SEC")
            quote = 0
            time.sleep(65)
            print(f"TIMEOUT END. QUOTE = {quote}")
        quote+=1
        worksheet.delete_rows(2)
        time.sleep(0.3)
    print(f"CLEAR QUOTE = {quote}. TIMEOUT 65 SEC")
    time.sleep(65)


if __name__ == '__main__':
    gs = gspread.service_account(filename='gs_credentials.json')  # подключаем файл с ключами и пр.
    sh = gs.open_by_key('17C7Ch7S9a3vHUIW3B8wGl7b_OYk9MuBRcssG6rbAGVQ')  # подключаем таблицу по ID
    worksheet = sh.sheet1  # получаем первый лист
    worksheet.format('M2:M100', {"numberFormat" : {"type": "DATE"}})
    worksheet.append_row(['Данные отсутствуют', 'mooon в ТРЦ Dana Mall', 'Зал 1 Premiere', 'Астерикс и Обеликс: Поднебесная', '32', 'Данные отсутствуют', 'ИСТИНА', '2023-03-01 21:00:00', 'Данные отсутствуют', 'Данные отсутствуют', 'Данные отсутствуют', 'Данные отсутствуют', '2023-03-01', 'Данные отсутствуют', '2D', 'Dolby Digital', 'Русский язык', 'Данные отсутствуют', 'зрителям, достигшим 12 лет', 'семейный, комедия, приключения'])

