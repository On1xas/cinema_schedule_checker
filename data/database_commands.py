import datetime
import os
import sqlite3
from config.config import table_th_names, room_names, theatre_names


# def insert_data_api_sql(show: tuple):
#     return f"INSERT INTO {table_th_names[theatre_names.index(show[0])]}_{room_names[theatre_names.index(show[0])].index(show[1]) + 1}_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#

def insert_data_tms_arena_sql(data_parsing_arena, cur, conn, date=str(datetime.date.today())):
    for show in data_parsing_arena:
        if date in show[1]:
            if show[0] == 'R1 S':
                cur.execute(
                    "INSERT INTO ARENA_1_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("Silver Screen в ТРЦ Arena city", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R2 S 3D DA':
                cur.execute(
                    "INSERT INTO ARENA_2_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("Silver Screen в ТРЦ Arena city", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R3 S':
                cur.execute(
                    "INSERT INTO ARENA_3_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("Silver Screen в ТРЦ Arena city", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R4 S 3D DA':
                cur.execute(
                    "INSERT INTO ARENA_4_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("Silver Screen в ТРЦ Arena city", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R5 S':
                cur.execute(
                    "INSERT INTO ARENA_5_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("Silver Screen в ТРЦ Arena city", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R6 S 3D':
                cur.execute(
                    "INSERT INTO ARENA_6_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("Silver Screen в ТРЦ Arena city", show[0], show[1], show[2], show[3]))
                conn.commit()


def insert_data_tms_palazzo_sql(data_parsing_palazzo, cur, conn, date=str(datetime.date.today())):
    for show in data_parsing_palazzo:
        if date in show[1]:
            if show[0] == 'R1 IMAX':
                cur.execute(
                    "INSERT INTO PALAZZO_1_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРЦ Palazzo", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R2 F':
                cur.execute(
                    "INSERT INTO PALAZZO_2_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРЦ Palazzo", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R3 F':
                cur.execute(
                    "INSERT INTO PALAZZO_3_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРЦ Palazzo", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R4 S':
                cur.execute(
                    "INSERT INTO PALAZZO_4_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРЦ Palazzo", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R5 F 3D':
                cur.execute(
                    "INSERT INTO PALAZZO_5_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРЦ Palazzo", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R6 F':
                cur.execute(
                    "INSERT INTO PALAZZO_6_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРЦ Palazzo", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R7 S':
                cur.execute(
                    "INSERT INTO PALAZZO_7_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРЦ Palazzo", show[0], show[1], show[2], show[3]))
                conn.commit()


def insert_data_tms_dana_sql(data_parsing_dana, cur, conn, date=str(datetime.date.today())):
    for show in data_parsing_dana:
        if date in show[1]:
            if show[0] == 'R1 S 3D DA':
                cur.execute(
                    "INSERT INTO DANA_1_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРЦ Dana Mall", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R2 F':
                cur.execute(
                    "INSERT INTO DANA_2_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРЦ Dana Mall", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R3 S SX':
                cur.execute(
                    "INSERT INTO DANA_3_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРЦ Dana Mall", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R4 S':
                cur.execute(
                    "INSERT INTO DANA_4_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРЦ Dana Mall", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R5 S 3D':
                cur.execute(
                    "INSERT INTO DANA_5_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРЦ Dana Mall", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R6 S':
                cur.execute(
                    "INSERT INTO DANA_6_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРЦ Dana Mall", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R7 S':
                cur.execute(
                    "INSERT INTO DANA_7_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРЦ Dana Mall", show[0], show[1], show[2], show[3]))
                conn.commit()


def insert_data_tms_triniti_sql(data_parsing_triniti, cur, conn, date=str(datetime.date.today())):
    for show in data_parsing_triniti:
        if date in show[1]:
            if show[0] == 'R1':
                cur.execute(
                    "INSERT INTO TRINITI_1_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРК Triniti", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R2 S':
                cur.execute(
                    "INSERT INTO TRINITI_2_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРК Triniti", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R3 F 3D':
                cur.execute(
                    "INSERT INTO TRINITI_3_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРК Triniti", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R4 S':
                cur.execute(
                    "INSERT INTO TRINITI_4_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРК Triniti", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R5 S':
                cur.execute(
                    "INSERT INTO TRINITI_5_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРК Triniti", show[0], show[1], show[2], show[3]))
                conn.commit()


def clear_parsing_all_table(cur, connect):
    for i in range(1, 7):
        sql = f"DELETE FROM ARENA_{i}_ROOM_API"
        cur.execute(sql)
        sql = f'DELETE FROM ARENA_{i}_ROOM_TMS'
        cur.execute(sql)
        connect.commit()
    for i in range(1, 8):
        sql = f"DELETE FROM PALAZZO_{i}_ROOM_API"
        cur.execute(sql)
        sql = f'DELETE FROM PALAZZO_{i}_ROOM_TMS'
        cur.execute(sql)
        connect.commit()
    for i in range(1, 8):
        sql = f"DELETE FROM DANA_{i}_ROOM_API"
        cur.execute(sql)
        sql = f'DELETE FROM DANA_{i}_ROOM_TMS'
        cur.execute(sql)
        connect.commit()
    for i in range(1, 6):
        sql = f"DELETE FROM TRINITI_{i}_ROOM_API"
        cur.execute(sql)
        sql = f'DELETE FROM TRINITI_{i}_ROOM_TMS'
        cur.execute(sql)
        connect.commit()
        if os.path.isfile(r'data/Schedule - BY_SS_ArenaCity.xlsx'):
            os.remove(r'data/Schedule - BY_SS_ArenaCity.xlsx')
            print(f'Временный файл Schedule - BY_SS_ArenaCity.xlsx был удален')
        if os.path.isfile(r'data/Schedule - BY_SS_Dana.xlsx'):
            os.remove(r'data/Schedule - BY_SS_Dana.xlsx')
            print(f'Временный файл Schedule - BY_SS_Dana.xlsx был удален')
        if os.path.isfile(r'data/Schedule - BY_SS_GrodnoTrinity.xlsx'):
            os.remove(r'data/Schedule - BY_SS_GrodnoTrinity.xlsx')
            print(f'Временный файл Schedule - BY_SS_GrodnoTrinity.xlsx был удален')
        if os.path.isfile(r'data/Schedule - BY_SS_Palazzo.xlsx'):
            os.remove(r'data/Schedule - BY_SS_Palazzo.xlsx')
            print(f'Временный файл Schedule - BY_SS_Palazzo.xlsx был удален')
    print(f'{"*" * 10}Очистка временных файлов и всех таблиц кинозалов выполнена успешно{"*" * 10}')


def delete_raw_sql(theathre, room, table_type, id_show):
    sql = f'DELETE FROM {theathre}_{room}_ROOM_{table_type} WHERE id = {id_show}'
    cur.execute(sql)
    connect.commit()


def prepare_set_show_from_db(cur):
    show_check = set()
    cur.execute(f'SELECT SHOW_NAME_API FROM PIVOT_SHOW_TABLE')
    for show in cur.fetchall():
        show_check.add(show[0])
    return show_check


def update_pivot_table(show_set_api, show_set_db, cursor, connect_db):
    print(f'***Обновляю информацию в сводной таблице***')
    for show in show_set_api:
        if show in show_set_db:
            sql = 'UPDATE PIVOT_SHOW_TABLE SET LAST_UPDATE = ? WHERE ? = SHOW_NAME_API;'
            cursor.execute(sql, (datetime.datetime.now(), show))
        else:
            sql = "INSERT INTO PIVOT_SHOW_TABLE (SHOW_NAME_API, LAST_UPDATE) VALUES (?,?)"
            cursor.execute(sql, (show, datetime.datetime.now()))
        connect_db.commit()


def fill_pivot_spl_title(cursor, connect_db):
    cursor.execute('SELECT * FROM PIVOT_SHOW_TABLE')
    for show in cursor.fetchall():
        if show[2] is None:
            spl_name = input(f'***Обнаружен фильм без данных о названии SPL. Введите название SPL к фильму {show[1]}\n')
            if spl_name == "":
                spl_name = None
            sql = "UPDATE PIVOT_SHOW_TABLE SET SPL_TITLE_NAME = ? WHERE id = ?;"
            cursor.execute(sql, (spl_name, show[0]))
            connect_db.commit()

# def insert_data_api_sql(show):
#     theatre = show[0]
#     room = show[1]
#     if theatre == 'mooon в ТРК Triniti':
#         if room == 'Зал 1':
#             return f"INSERT INTO TRINITI_1_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 2 Lounge':
#             return f"INSERT INTO TRINITI_2_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 3 Premiere':
#             return f"INSERT INTO TRINITI_3_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 4 Resto':
#             return f"INSERT INTO TRINITI_4_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 5 VIP':
#             return f"INSERT INTO TRINITI_5_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#     if theatre == 'mooon в ТРЦ Dana Mall':
#         if room == 'Зал 1 Premiere':
#             return f"INSERT INTO DANA_1_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 2':
#             return f"INSERT INTO DANA_2_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 3 Screen X':
#             return f"INSERT INTO DANA_3_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 4 Vegas lounge':
#             return f"INSERT INTO DANA_4_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 5':
#             return f"INSERT INTO DANA_5_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 6 VIP':
#             return f"INSERT INTO DANA_6_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 7 VIP':
#             return f"INSERT INTO DANA_7_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#
#     if theatre == 'mooon в ТРЦ Palazzo':
#         if room == 'Зал 1 mooon IMAX':
#             return f"INSERT INTO PALAZZO_1_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 2 Vegas':
#             return f"INSERT INTO PALAZZO_2_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 3 VIP':
#             return f"INSERT INTO PALAZZO_3_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 4 Resto':
#             return f"INSERT INTO PALAZZO_4_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 5 mooon+  ':
#             return f"INSERT INTO PALAZZO_5_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 6 Kids':
#             return f"INSERT INTO PALAZZO_6_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 7 Visa Premiere':
#             return f"INSERT INTO PALAZZO_7_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#     if theatre == 'Silver Screen в ТРЦ Arena city':
#         if room == 'Зал 1':
#             return f"INSERT INTO ARENA_1_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 2':
#             return f"INSERT INTO ARENA_2_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 3':
#             return f"INSERT INTO ARENA_3_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 4':
#             return f"INSERT INTO ARENA_4_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
#         if room == 'Зал 5':
#             return f'INSERT INTO ARENA_5_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)'
#         if room == 'Зал 6':
#             return f"INSERT INTO ARENA_6_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT, AUDIO) VALUES(?,?,?,?,?,?)"
