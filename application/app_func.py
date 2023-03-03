
import sqlite3


def update_pivot_raw(spl_name, id):
    with sqlite3.connect('data\database.db') as db:
        cursor = db.cursor()
        sql = f'UPDATE PIVOT_SHOW_TABLE SET SPL_TITLE_NAME = ? WHERE id = ?'
        cursor.execute(sql, (spl_name, id))
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
        table.delete(item)
    print('Таблица была очищена')


def load_table_info(self):
    data = get_pivot_info()
    for item in data:
        self.insert("", 'end', values=item)


def delete_select_raw(table):
    item = table.selection()
    p_id = table.item(item)
    print(f"{p_id['values'][1]} УДАЛЕН ИЗ DB")
    with sqlite3.connect('data\database.db') as db:
        cursor = db.cursor()
        sql='DELETE FROM PIVOT_SHOW_TABLE WHERE SHOW_NAME_API = ?'
        cursor.execute(sql, (p_id['values'][1],))
        db.commit()
    table.delete(item)

 #   print(, p_id['values'][1]) # точка удаления строки из БД [38, ' Снежная королева: Разморозка ', 'SQ', '2023-02-22 14:47:05.334527']


