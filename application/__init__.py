import tkinter
from tkinter import *
from tkinter import ttk
import sqlite3
import os


def set_spl_name():
    spl = new_spl_name.get()
    iid = id_show.get()
    sql = f'UPDATE PIVOT_SHOW_TABLE SET SPL_TITLE_NAME = ? WHERE id = ?'
    cursor.execute(sql, (spl, iid))
    connect.commit()
    print(f'SPL NAME: {spl} добавлен к ID {iid}')


window = Tk()
window.geometry('300x100')
window.title('Обновление сводной таблицы')
window.resizable(False, False)
window.iconbitmap()
tkinter.Label(window, text='Новые данные').grid(row=0, column=1, sticky='w')
tkinter.Label(window, text='id в таблице').grid(row=1, column=0, sticky='w')
id_show = tkinter.Entry(window)
id_show.grid(row=1, column=1)
tkinter.Label(window, text='Новое название SPL').grid(row=2, column=0, sticky='w')
new_spl_name = tkinter.Entry(window)
new_spl_name.grid(row=2, column=1)
ttk.Button(window, text='Отправить в БД', command=set_spl_name).grid(row=3, column=1, sticky='we')
window.grid_columnconfigure(0, minsize=100)
window.grid_columnconfigure(1, minsize=100)
window.grid_columnconfigure(2, minsize=100)
connect = sqlite3.connect(f'{os.getcwd()}\data\database.db')
cursor = connect.cursor()
sql = f'SELECT id, SHOW_NAME_API, SPL_TITLE_NAME FROM PIVOT_SHOW_TABLE'
cursor.execute(sql)
for show in cursor.fetchall():
    print(str(f"ID {show[0]}").rjust(7), end="  ")
    print(str(f"{show[1]}").ljust(50), end="")
    print(str(f"SPL: {show[2]}").ljust(50))
print()
window.mainloop()
