import sqlite3

from data.database_commands import prepare_set_show_from_db, insert_data_api_sql, update_pivot_table, clear_parsing_all_table, fill_pivot_spl_title
from parsing.parse_cinema_api import parse_schedule_api

show_set_api=set()


def main():
    pass


if __name__ == '__main__':
    connect_db=sqlite3.connect('data\database.db')
    cur=connect_db.cursor()
    # Очистка таблиц от предыдущих данных сеансов
    clear_parsing_all_table(cur, connect_db)
    #Подготавливаем множество названий сеансов которое знает база данных
    show_set_db=prepare_set_show_from_db(cur)
    # Запрашиваем сеансы из программного обеспечения букера
    parse_api=parse_schedule_api()
    # Вносим данные в таблицы залов и ищем новые сеансы о которых не знает система, добавляем
    for show in parse_api:
        # Подготавливаем SQL запрос на добавления данных в таблицу залов
        sql=insert_data_api_sql(show)
        show_set_api.add(show[3])
        # Отправляем запрос INSERT в БД и передаем в него кортеж сеанса
        cur.execute(sql, show)
        connect_db.commit()
    # Обновляем сводную таблицу. При нахождении новых сеансов, добавляем их в таблицу.
    update_pivot_table(show_set_api,show_set_db,cur,connect_db)
    # Заполняем графу SPL_TITLE в сводной таблице.
    fill_pivot_spl_title(cur,connect_db)
    connect_db.close()
