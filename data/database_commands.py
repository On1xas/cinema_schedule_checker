import sqlite3


def insert_data_api_sql(show):
    theatre = show[0]
    room = show[1]
    if theatre == 'mooon в ТРК Triniti':
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
        if room == 'Зал 1':
            return f"INSERT INTO ARENA_1_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 2':
            return f"INSERT INTO ARENA_2_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 3':
            return f"INSERT INTO ARENA_3_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 4':
            return f"INSERT INTO ARENA_4_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"
        if room == 'Зал 5':
            return f'INSERT INTO ARENA_5_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)'
        if room == 'Зал 6':
            return f"INSERT INTO ARENA_6_ROOM_API (TH_NAME, ROOM, SHOW_TIME, SHOW_NAME, FORMAT) VALUES(?,?,?,?,?)"

def insert_data_tms_sql(show):
    with open() as file:
        pass

def clear_parsing_all_table():
    connect=sqlite3.connect('..\data\database.db')
    cur=connect.cursor()
    for i in range(1,7):
        sql=f"DELETE FROM ARENA_{i}_ROOM_API"
        cur.execute(sql)
        sql = f'DELETE FROM ARENA_{i}_ROOM_TMS'
        cur.execute(sql)
        connect.commit()
    for i in range(1,8):
        sql=f"DELETE FROM PALAZZO_{i}_ROOM_API"
        cur.execute(sql)
        sql = f'DELETE FROM PALAZZO_{i}_ROOM_TMS'
        cur.execute(sql)
        connect.commit()
    for i in range(1,8):
        sql=f"DELETE FROM DANA_{i}_ROOM_API"
        cur.execute(sql)
        sql = f'DELETE FROM DANA_{i}_ROOM_TMS'
        cur.execute(sql)
        connect.commit()
    for i in range(1,6):
        sql=f"DELETE FROM TRINITI_{i}_ROOM_API"
        cur.execute(sql)
        sql = f'DELETE FROM TRINITI_{i}_ROOM_TMS'
        cur.execute(sql)
        connect.commit()
    connect.close()
    print(f'{clear_parsing_all_table.__name__}***Очистка всех таблиц кинозалов выполнена успешно***')

def delete_raw_sql(theathre, room,table_type, id_show):
    connect=sqlite3.connect('..\data\database.db')
    cur=connect.cursor()
    sql=f'DELETE FROM {theathre}_{room}_ROOM_{table_type} WHERE id = {id_show}'
    cur.execute(sql)
    connect.commit()
    connect.close()

def prepare_set_show_from_db():
    show_check = set()
    cur.execute(f'SELECT SHOW_NAME_API FROM PIVOT_SHOW_TABLE')
    for show in cur.fetchall():
        show_check.add(show[0])
    return show_check