import datetime
import sqlite3

# show=('mooon в ТРЦ Palazzo', 'Зал 7 Visa Premiere', '2023-2-14T11:10:00', ' Мой домашний крокодил ', '2D')
# show_set={' Одиноки вместе ', ' Амстердам ', ' Операция «Фортуна»: Искусство побеждать ', ' mooon LOVE PARTY ', ' Форма голоса (RU SUB) ', ' Заклятие Абизу ', ' Мой домашний крокодил ', ' Свободные отношения ', ' Кот в сапогах 2: Последнее желание ', ' Непослушная ', ' М3ГАН ', ' Аватар: Путь воды ', ' Изумительный Морис ', ' Форма голоса ', ' Чебурашка ', ' Знакомство родителей '}
# show_set_api = {' Непослушная ', ' Форма голоса ', ' Аватар: Путь воды ', ' Одиноки вместе ', ' Мой домашний крокодил ',
#                 ' Изумительный Морис ', ' Операция «Фортуна»: Искусство побеждать ', ' М3ГАН ',
#                 ' Кот в сапогах 2: Последнее желание ', ' mooon LOVE PARTY ', ' Заклятие Абизу ',
#                 ' Знакомство родителей ', ' Амстердам ', ' Свободные отношения ', ' Форма голоса (RU SUB) ',
#                 ' Чебурашка '}
# show_set_db = {' Непослушная ', ' Форма голоса ', ' Одиноки вместе ', ' Аватар: Путь воды ', ' Мой домашний крокодил ',
#                ' Операция «Фортуна»: Искусство побеждать ', ' Изумительный Морис ', ' М3ГАН ',
#                ' Кот в сапогах 2: Последнее желание ', ' mooon LOVE PARTY ', ' Заклятие Абизу ',
#                ' Знакомство родителей ', ' Амстердам ', ' Свободные отношения ', ' Форма голоса (RU SUB) ',
#                ' Чебурашка '}

connect_db = sqlite3.connect('..\data\database.db')
cursor = connect_db.cursor()
#
# for show in show_set:
#     cur.execute(f'INSERT INTO PIVOT_SHOW_TABLE (SHOW_NAME_API, LAST_UPDATE) VALUES(?,?)',
#                 (show, datetime.datetime.now()))
#     connect.commit()

# cursor.execute('DELETE FROM PIVOT_SHOW_TABLE')
# connect_db.commit()

# cursor.execute('SELECT * FROM PIVOT_SHOW_TABLE')
# for show in cursor.fetchall():
#     print(show)
#     if show[2] is None:
#         spl_name=input(f'***Обнаружен фильм без данных о названии SPL. Введите название SPL к фильму {show[1]}\n')
#         sql = "UPDATE PIVOT_SHOW_TABLE SET SPL_TITLE_NAME = ? WHERE id = ?;"
#         cursor.execute(sql, (spl_name, show[0]))
#         connect_db.commit()
connect_db.close()
