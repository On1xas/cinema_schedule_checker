from parsing.parse_cinema_api import *
import gspread
import time
from application.app_func import get_show_from_api

def connect_gsdb():
    gs = gspread.service_account(filename='gs_credentials.json')  # подключаем файл с ключами и пр.
    sh = gs.open_by_key('17C7Ch7S9a3vHUIW3B8wGl7b_OYk9MuBRcssG6rbAGVQ')  # подключаем таблицу по ID
    worksheet = sh.sheet1  # получаем первый лист
    return worksheet
def add_show_gsdb():
    worksheet= connect_gsdb()
    data=get_show_from_api()
    if len(data)>299:
        for item in data[:290]:
            worksheet.append_row(item)
            time.sleep(0.2)
        time.sleep(65)
        for item in data[290:]:
            worksheet.append_row(item)
            time.sleep(0.2)
    else:
        for item in data:
            worksheet.append_row(item)
            time.sleep(0.2)
def clear_gsdb():
    worksheet= connect_gsdb()
    time.sleep(2)
    for row in range(1, len(worksheet.col_values(1))):
        worksheet.delete_rows(2)
        time.sleep(0.2)

if __name__ == '__main__':
    clear_gsdb()
    add_show_gsdb()