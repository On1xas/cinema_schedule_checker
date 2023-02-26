import sqlite3


def update_pivot_raw(spl_name,id):
    with sqlite3.connect('../data/database.db') as db:
        cursor = db.cursor()
        sql = f'UPDATE PIVOT_SHOW_TABLE SET SPL_TITLE_NAME = ? WHERE id = ?'
        cursor.execute(sql,(spl_name,id))
        db.commit()

def get_pivot_info():
    with sqlite3.connect('../data/database.db') as db:
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

if __name__ == '__main__':
    print(get_pivot_info())