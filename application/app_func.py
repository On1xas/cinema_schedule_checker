import datetime
import sqlite3

import colorama as colorama

from data.database_commands import clear_parsing_all_table, prepare_set_show_from_db, update_pivot_table, \
    fill_pivot_spl_title, insert_data_tms_palazzo_sql, insert_data_tms_arena_sql, insert_data_tms_dana_sql, \
    insert_data_tms_triniti_sql
from parsing.parse_cinema_api import parse_schedule_api
from config.config import table_th_names, room_names, theatre_names
from parsing.parsing_arena import parser_tms_arena
from parsing.parsing_dana import parser_tms_dana
from parsing.parsing_palazzo import parser_tms_palazzo
from parsing.parsing_triniti import parser_tms_triniti


def update_pivot_raw(spl_name, id):
    with sqlite3.connect('data\database.db') as db:
        print("Connected DB")
        cursor = db.cursor()
        sql = f'UPDATE PIVOT_SHOW_TABLE SET SPL_TITLE_NAME = ? WHERE id = ?'
        cursor.execute(sql, (spl_name, id))
        print("commit")
        db.commit()


def get_pivot_info():
    with sqlite3.connect('data\database.db') as db:
        cursor = db.cursor()
        sql = f'SELECT * FROM PIVOT_SHOW_TABLE'
        cursor.execute(sql)
        data = cursor.fetchall()
        return data


def clear_table(table):
    for item in table.get_children():
        print(item)
        table.delete(item)
    print('Таблица была очищена')


def load_table_info(self):
    data = get_pivot_info()
    for item in data:
        print(item)
        self.insert("", 'end', values=item)


def delete_select_raw(table):
    item = table.selection()
    p_id = table.item(item)
    print(f"{p_id['values'][1]} УДАЛЕН ИЗ DB")
    with sqlite3.connect('data\database.db') as db:
        cursor = db.cursor()
        sql = 'DELETE FROM PIVOT_SHOW_TABLE WHERE SHOW_NAME_API = ?'
        cursor.execute(sql, (p_id['values'][1],))
        db.commit()
    table.delete(item)

 #   print(, p_id['values'][1]) # точка удаления строки из БД [38, ' Снежная королева: Разморозка ', 'SQ', '2023-02-22 14:47:05.334527']
def check_show(theatre, rooms, cursor):
    colorama.init()
    for room in range(1, rooms + 1):
        show_api = []
        show_tms = []
        print(f'{"*" * 10} ПРОВЕРКА КИНОТЕАТРА {theatre} ЗАЛ {room}  {"*" * 10}')
        tmpl = f'SELECT SHOW_NAME, SHOW_TIME, FORMAT, AUDIO FROM {theatre}_{room}_ROOM_API'
        cursor.execute(tmpl)
        for show in cursor.fetchall():
            show_api.append(
                (show[0], show_dict[show[0]], str(datetime.datetime.strptime(show[1], '%Y-%m-%dT%H:%M:%S')), show[2],
                 show[3]))

        tmpl = f'SELECT SPL_TITLE, SHOW_START FROM {theatre}_{room}_ROOM_TMS'
        cursor.execute(tmpl)
        for show in cursor.fetchall():
            show_tms.append((show[0],
                             str(datetime.datetime.strptime(show[1][:19], '%Y-%m-%dT%H:%M:%S') + datetime.timedelta(
                                 minutes=10))))
        for show in show_api:
            error_reason = ''
            for showtms in show_tms:
                flag_spl = show[1] in showtms[0]
                flag_time = show[2] == showtms[1]
                if flag_time and flag_spl:
                    print(
                        colorama.Fore.GREEN + f'Сеанс {show[0]} в {show[2][11:-3]} GOOD {colorama.Fore.BLUE if show[3] == "3D" else colorama.Fore.GREEN} {show[3]} {colorama.Fore.GREEN if show[4] == "RU-RU" else colorama.Fore.RED} {show[4]}')

                    print(colorama.Style.RESET_ALL, end='')
                    break
                if flag_time == True and flag_spl == False:
                    error_reason = 'Время сеанса корректное. Неверный SPL или название SPL в базе.'
            else:
                if error_reason == "":
                    error_reason = 'Неверное время сеанса в TMS или сеанса нет в TMS'
                print(
                    colorama.Fore.RED + f'Сеанс {show[0]} в {show[2][11:-3]} BAD. {colorama.Fore.BLUE if show[3] == "3D" else colorama.Fore.GREEN} {show[3]} {colorama.Fore.YELLOW if show[4] == "RU-RU" else colorama.Fore.RED} {show[4]} {colorama.Fore.RED} REASON: {error_reason}')
                print(colorama.Style.RESET_ALL, end='')
def start_parse(date, show_set_api=set()):
    connect_db = sqlite3.connect('data\database.db')
    cur = connect_db.cursor()
    # # Очистка таблиц от предыдущих данных сеансов
    clear_parsing_all_table(cur, connect_db)
    # # Подготавливаем множество названий сеансов которое знает база данных
    show_set_db = prepare_set_show_from_db(cur)
    # Запрашиваем сеансы из программного обеспечения букера
    parse_api = parse_schedule_api(date)
    # Вносим данные в таблицы залов и ищем новые сеансы о которых не знает система, добавляем
    for show in parse_api:
        # Подготавливаем SQL запрос на добавления данных в таблицу залов
        sql = f"INSERT INTO {table_th_names[theatre_names.index(show[0])]}_{room_names[theatre_names.index(show[0])].index(show[1]) + 1}_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?) "
        show_set_api.add(show[3])
        # Отправляем запрос INSERT в БД и передаем в него кортеж сеанса
        cur.execute(sql, show)
        connect_db.commit()
    # Обновляем сводную таблицу. При нахождении новых сеансов, добавляем их в таблицу.
    update_pivot_table(show_set_api, show_set_db, cur, connect_db)
    # Заполняем графу SPL_TITLE в сводной таблице.
    fill_pivot_spl_title(cur, connect_db)
    # Выполняем парсинг серверов TMS и вносим данные в БД по залам
    insert_data_tms_palazzo_sql(parser_tms_palazzo(), cur, connect_db,date)
    insert_data_tms_arena_sql(parser_tms_arena(), cur, connect_db,date)
    insert_data_tms_dana_sql(parser_tms_dana(), cur, connect_db,date)
    insert_data_tms_triniti_sql(parser_tms_triniti(), cur, connect_db,date)
    # # Подготавливаем словарь с названием фильма = название SPL
    show_dict = dict()
    tmpl = f'SELECT SHOW_NAME_API,SPL_TITLE_NAME FROM PIVOT_SHOW_TABLE'
    cur.execute(tmpl)
    for show in cur.fetchall():
        show_dict[show[0]] = show[1]
    # Делаем сверку сеансов кинотеатров
    check_show('PALAZZO', len(room_names[0]), cur)
    check_show('ARENA', len(room_names[1]), cur)
    check_show('DANA', len(room_names[2]), cur)
    check_show('TRINITI', len(room_names[3]), cur)

    connect_db.close()
