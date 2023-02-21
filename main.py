import sqlite3

from data.database_commands import prepare_set_show_from_db, insert_data_api_sql, update_pivot_table, \
    clear_parsing_all_table, fill_pivot_spl_title, insert_data_tms_palazzo_sql, insert_data_tms_triniti_sql, \
    insert_data_tms_dana_sql, insert_data_tms_arena_sql
from parsing.parse_cinema_api import parse_schedule_api
from parsing.parsing_arena import parser_tms_arena
from parsing.parsing_triniti import parser_tms_triniti
from parsing.parsing_dana import parser_tms_dana
from parsing.parsing_palazzo import parser_tms_palazzo
import datetime
import colorama

show_set_api = set()


def check_show(theatre, cursor):
    colorama.init()
    if theatre.upper() == 'ARENA':
        rooms = 6
    elif theatre.upper() == 'DANA':
        rooms = 7
    elif theatre.upper() == 'PALAZZO':
        rooms = 7
    elif theatre.upper() == 'TRINITI':
        rooms = 5
    for room in range(1, rooms + 1):
        show_api = []
        show_tms = []
        print(f'{"*" * 10} ПРОВЕРКА КИНОТЕАТРА {theatre} ЗАЛ {room}  {"*" * 10}')
        tmpl = f'SELECT SHOW_NAME, SHOW_TIME FROM {theatre}_{room}_ROOM_API'
        cursor.execute(tmpl)
        for show in cursor.fetchall():
            show_api.append(
                (show[0], show_dict[show[0]], str(datetime.datetime.strptime(show[1], '%Y-%m-%dT%H:%M:%S'))))

        tmpl = f'SELECT SPL_TITLE, SHOW_START FROM {theatre}_{room}_ROOM_TMS'
        cursor.execute(tmpl)
        for show in cursor.fetchall():
            show_tms.append((show[0],
                             str(datetime.datetime.strptime(show[1][:19], '%Y-%m-%dT%H:%M:%S') + datetime.timedelta(
                                 minutes=10))))
        for show in show_api:
            error_reason=''
            for showtms in show_tms:
                flag_spl = show[1] in showtms[0]
                flag_time = show[2] == showtms[1]
                if flag_time and flag_spl:
                    print(colorama.Fore.GREEN + f'Сеанс {show[0]} в {show[2][11:-3]} GOOD')
                    print(colorama.Style.RESET_ALL, end='')
                    break
                if flag_time == True and flag_spl == False:
                    error_reason='Время сеанса корректное. Неверный SPL или название SPL в базе.'
            else:
                if error_reason=="":
                    error_reason='Неверное время сеанса в TMS или сеанса нет в TMS'
                print(colorama.Fore.RED + f'Сеанс {show[0]} в {show[2][11:-3]} BAD. REASON: {error_reason}')
                print(colorama.Style.RESET_ALL, end='')


if __name__ == '__main__':
    connect_db = sqlite3.connect('data\database.db')
    cur = connect_db.cursor()
    # Очистка таблиц от предыдущих данных сеансов
    clear_parsing_all_table(cur, connect_db)
    # Подготавливаем множество названий сеансов которое знает база данных
    show_set_db = prepare_set_show_from_db(cur)
    # Запрашиваем сеансы из программного обеспечения букера
    parse_api = parse_schedule_api()
    # Вносим данные в таблицы залов и ищем новые сеансы о которых не знает система, добавляем
    for show in parse_api:
        # Подготавливаем SQL запрос на добавления данных в таблицу залов
        sql = insert_data_api_sql(show)
        show_set_api.add(show[3])
        # Отправляем запрос INSERT в БД и передаем в него кортеж сеанса
        cur.execute(sql, show)
        connect_db.commit()
    # Обновляем сводную таблицу. При нахождении новых сеансов, добавляем их в таблицу.
    update_pivot_table(show_set_api, show_set_db, cur, connect_db)
    # Заполняем графу SPL_TITLE в сводной таблице.
    fill_pivot_spl_title(cur, connect_db)
    # Выполняем парсинг серверов TMS и вносим данные в БД по залам
    insert_data_tms_arena_sql(parser_tms_arena(), cur, connect_db)
    insert_data_tms_dana_sql(parser_tms_dana(), cur, connect_db)
    insert_data_tms_palazzo_sql(parser_tms_palazzo(), cur, connect_db)
    insert_data_tms_triniti_sql(parser_tms_triniti(), cur, connect_db)
    show_dict = dict()
    tmpl = f'SELECT SHOW_NAME_API,SPL_TITLE_NAME FROM PIVOT_SHOW_TABLE'
    cur.execute(tmpl)
    for show in cur.fetchall():
        show_dict[show[0]] = show[1]
    check_show('ARENA', cur)
    check_show('PALAZZO', cur)
    check_show('DANA', cur)
    check_show('TRINITI', cur)

    connect_db.close()
