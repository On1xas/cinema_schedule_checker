import sqlite3
import datetime
import requests
from lxml import etree
import xml.etree.ElementTree as ET
import colorama

def update_pivot_raw(spl_name,id):
    with sqlite3.connect('data\database.db') as db:
        cursor = db.cursor()
        sql = f'UPDATE PIVOT_SHOW_TABLE SET SPL_TITLE_NAME = ? WHERE id = ?'
        cursor.execute(sql,(spl_name,id))
        db.commit()

def get_pivot_info():
    with sqlite3.connect('data\database.db') as db:
        cursor=db.cursor()
        sql=f'SELECT * FROM PIVOT_SHOW_TABLE'
        cursor.execute(sql)
        data=cursor.fetchall()
        return data

def clear_table(table):
    for item in table.get_children():
        table.delete(item)
    print('Таблица была очищена')

def load_table_info(table):
    data=get_pivot_info()
    for item in data:
        table.insert("", 'end', values=item)

def delete_select_raw(table):
    item=table.selection()
    table.delete(item)

# def get_show_from_api(dates=datetime.datetime.now().date()):
#
#     data_parsing_api = []
#     colorama.init()
#     url = f'{parsing_url_api}{dates}'
#     print(
#             f"***Выполняю запрос сеансов на {colorama.Fore.RED} {dates} {colorama.Style.RESET_ALL} из программного обеспечения кинотеатра***")
#     request = requests.get(url)
#     if request.status_code == 200:
#         print(f'***Ответ получен успешно***')
#         xml = request.text
#         parser = etree.XMLParser(recover=True)
#         root = ET.fromstring(xml, parser=parser)
#         for i in range(1, len(root[0])):
#             date = datetime.datetime.strptime(root[0][i][2].text, '%Y-%m-%dT%H:%M:%S')
#             data_parsing_api.append(("Данные отсутствуют",
#                                     root[0][i][29].text,
#                                     root[0][i][28].text,
#                                     root[0][i][15].text,
#                                     root[0][i][40].text,
#                                     "Данные отсутствуют",
#                                     "ИСТИНА",
#                                     str(date)+".0",
#                                     "Данные отсутствуют",
#                                     "Данные отсутствуют",
#                                     "Данные отсутствуют",
#                                     "Данные отсутствуют",
#                                     str(date.date()),
#                                     "Данные отсутствуют",
#                                     root[0][i][34].text,
#                                     "Dolby Digital",
#                                     "Русский язык",
#                                     "Данные отсутствуют",
#                                     root[0][i][20].text,
#                                     root[0][i][24].text
#                                     ))
#         return list(sorted(data_parsing_api, key=lambda x: x[2]))
#     else:
#         print(
#                 f"""***Проверьте полученные данные, возможно запрос был выполнен некорректно или не выполнен вовсе. Ошибка запроса {request.status_code}.***""")
#         return None
# if __name__ == '__main__':
    # for item in get_show_from_api():
    #     print(item)
    # date=datetime.datetime.strptime('2023-2-28T21:00:00', '%Y-%m-%dT%H:%M:%S')
    # print(date.date())
    # print(date.time())