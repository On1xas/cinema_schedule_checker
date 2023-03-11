import gspread
import datetime
import colorama
import requests
from lxml import etree
import xml.etree.ElementTree as ET
from config.config import parsing_url_api


def connect_gsdb():
    gs = gspread.service_account(filename='parsing/gs_credentials.json')  # подключаем файл с ключами и пр.
    sh = gs.open_by_key('17C7Ch7S9a3vHUIW3B8wGl7b_OYk9MuBRcssG6rbAGVQ')  # подключаем таблицу по ID
    worksheet = sh.sheet1  # получаем первый лист

    print('Google Sheet - CinemaShowDB Connected')
    #    print(len(worksheet.get_all_values()))
    return worksheet


def add_show_gsdb(date=datetime.datetime.now().date()):
    date=date
    worksheet = connect_gsdb()
    worksheet.batch_clear(['A2:T500'])
    print('CinemaShowDB была очищена')
    data = get_show_from_api(date)
    worksheet.update(f"A2:T{len(data) + 1}", data)
    print(f"Было загружено {len(data)} сеансов")


def clear_gsdb():
    worksheet = connect_gsdb()
    worksheet.batch_clear(['A2:T500'])
    print('CinemaShowDB была очищена')

def get_show_from_api(dates=datetime.datetime.now().date()):
    data_parsing_api = []
    colorama.init()
    url = f'{parsing_url_api}{dates}'
    print(
        f"***Выполняю запрос сеансов на {colorama.Fore.RED} {dates} {colorama.Style.RESET_ALL} из программного обеспечения кинотеатра***")
    request = requests.get(url)
    if request.status_code == 200:
        print(f'***Ответ получен успешно***')
        xml = request.text
        parser = etree.XMLParser(recover=True)
        root = ET.fromstring(xml, parser=parser)
        for i in range(1, len(root[0])):
            date = datetime.datetime.strptime(root[0][i][2].text, '%Y-%m-%dT%H:%M:%S')
            data_parsing_api.append(("Данные отсутствуют",
                                     root[0][i][29].text,
                                     root[0][i][28].text,
                                     root[0][i][15].text.strip(),
                                     root[0][i][40].text,
                                     "Данные отсутствуют",
                                     "ИСТИНА",
                                     root[0][i][2].text,
                                     "Данные отсутствуют",
                                     "Данные отсутствуют",
                                     "Данные отсутствуют",
                                     "Данные отсутствуют",
                                     str(date.date()),
                                     "Данные отсутствуют",
                                     root[0][i][34].text,
                                     "Dolby Digital",
                                     "Русский язык",
                                     "Данные отсутствуют",
                                     root[0][i][20].text,
                                     root[0][i][24].text
                                     ))
        return list(sorted(data_parsing_api, key=lambda x: x[2]))
    else:
        print(
            f"""***Проверьте полученные данные, возможно запрос был выполнен некорректно или не выполнен вовсе. Ошибка запроса {request.status_code}.***""")
        return None

if __name__ == '__main__':
    add_show_gsdb()


















# def get_show_from_api(dates=datetime.datetime.now().date()):
#     data_parsing_api = []
#     colorama.init()
#     url = f'{parsing_url_api}{dates}'
#     print(
#         f"***Выполняю запрос сеансов на {colorama.Fore.RED} {dates} {colorama.Style.RESET_ALL} из программного обеспечения кинотеатра***")
#     request = requests.get(url)
#     if request.status_code == 200:
#         print(f'***Ответ получен успешно***')
#         xml = request.text
#         parser = etree.XMLParser(recover=True)
#         root = ET.fromstring(xml, parser=parser)
#         for i in range(1, len(root[0])):
#             date = datetime.datetime.strptime(root[0][i][2].text, '%Y-%m-%dT%H:%M:%S')
#             data_parsing_api.append(("Данные отсутствуют",
#                                      root[0][i][29].text,
#                                      root[0][i][28].text,
#                                      root[0][i][15].text.strip(),
#                                      root[0][i][40].text,
#                                      "Данные отсутствуют",
#                                      "ИСТИНА",
#                                      root[0][i][2].text,
#                                      "Данные отсутствуют",
#                                      "Данные отсутствуют",
#                                      "Данные отсутствуют",
#                                      "Данные отсутствуют",
#                                      str(date.date()),
#                                      "Данные отсутствуют",
#                                      root[0][i][34].text,
#                                      "Dolby Digital",
#                                      "Русский язык",
#                                      "Данные отсутствуют",
#                                      root[0][i][20].text,
#                                      root[0][i][24].text
#                                      ))
#         return list(sorted(data_parsing_api, key=lambda x: x[2]))
#     else:
#         print(
#             f"""***Проверьте полученные данные, возможно запрос был выполнен некорректно или не выполнен вовсе. Ошибка запроса {request.status_code}.***""")
#         return None