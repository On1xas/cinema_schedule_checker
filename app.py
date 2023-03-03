import sqlite3
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry, Calendar
from application.app_func import update_pivot_raw, clear_table, load_table_info, delete_select_raw, get_pivot_info


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Тут будет название приложения')
        self.iconbitmap()
        self.minsize(1200, 800)
        self.ini_frames()

    def ini_frames(self):
        Frame_control(self).place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
        Frame_table(self).place(relx=0, rely=0, relwidth=0.5, relheight=1)

    def clear_data_in_db(self):
        update_pivot_raw(*self.get_id_and_spl_name())
        clear_table(self)
        load_table_info(self)
        self.delete_entry_id_spl()


    def get_id_and_spl_name(self):
        id=self.entry_id_label.get()
        spl=self.entry_new_spl_name.get()
        return (spl, id)

    def delete_entry_id_spl(self):
        self.entry_id_label.delete(0, tk.END)
        self.entry_new_spl_name.delete(0, tk.END)

    def clear_table(self):
        for item in self.table.get_children():
            self.delete(item)
        print('Таблица была очищена')

    def load_table_info(self):
        data = get_pivot_info()
        for item in data:
            self.insert("", 'end', values=item)




class Frame_table(tk.Frame, App):

    def __init__(self, app):
        super().__init__(app)
        self['background'] = 'yellow'
        self.put_widgets()

    def put_widgets(self):
        # Создаем виджет Treeview (аналог таблицы)
        self.table = ttk.Treeview(self, show='headings')

        # Задаем название стобцов
        heads = ['id', 'SHOW_NAME', 'SPL_TITLE']
        # Присватваем параметру "colums" название столбцов
        self.table['columns'] = heads

        # Передаем данные в таблицу. Вносим заголовки столбцов и выравниваем их по центру
        for head in heads:
            self.table.heading(head, text=head, anchor='center')
            # Передаем команду что данные в ячейках столбцов должна быть поцентру
            self.table.column(head, anchor='center')

        load_table_info(self.table)

        scr_panel = ttk.Scrollbar(self, command=self.table.yview)
        scr_panel.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.configure(yscrollcommand=scr_panel.set)
        self.table.pack(expand=tk.YES, fill=tk.BOTH, anchor='w')

    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)
        print('Таблица была очищена')

class Frame_control(tk.Frame, App):
    def __init__(self, app):
        super().__init__(app)
        self['background'] = 'black'
        self.put_widgets()

    def put_widgets(self):
        ### БЛОК ИЗМЕНЕНИЯ НАЗВАНИЯ ПЛЕЙЛИСТА
        ### ----------------------------------------------------------------------------------------
        txt_title_spl_update = ttk.Label(self, text="Обновление данных в таблице")
        txt_entry_id = ttk.Label(self, text="Введите ID сеанса")
        txt_entry_new_spl_name = ttk.Label(self, text="Введите новое название SPL")
        self.entry_id_label = ttk.Entry(self)
        self.entry_new_spl_name = ttk.Entry(self)
        button_id = ttk.Button(self, text='Обновить данные в БД', command=self.clear_data_in_db)

        txt_title_spl_update.grid(row="0", column="1", padx=3, pady=3)
        txt_entry_id.grid(row="1", column="0", padx=3, pady=3)
        txt_entry_new_spl_name.grid(row="2", column="0", padx=3, pady=3)
        self.entry_id_label.grid(row='1', column='1')
        self.entry_new_spl_name.grid(row='2', column='1')
        button_id.grid(row="3", column="1", padx=3, pady=3)
        ### ----------------------------------------------------------------------------------------
        txt_title_button_clear_raw = ttk.Label(self,
                                               text="Если прокат фильма закончился \n Выберите в таблице строку для удаления")
        button_id = ttk.Button(self, text='Удалить строку')

        txt_title_button_clear_raw.grid(row="4", column="1", padx=3, pady=3)
        button_id.grid(row="5", column="1", padx=3, pady=3)
        ### ----------------------------------------------------------------------------------------
        ### Раздел ОБНОВЛЕНИЯ ГУГЛ ТАБЛИЦЫ ЧБОБО
        txt_title_update_gs = ttk.Label(self, text="Обновленние ВЫГРУЗКИ в таблице расписания чбобо")
        txt_calendar_gs = ttk.Label(self, text="\tВыберите дату \n \tдля выгрузки данных")
        calendar_update_gs = DateEntry(self, date_pattern="YYYY-mm-dd")
        button_update_gs = ttk.Button(self, text="Обновить таблицу")

        txt_title_update_gs.grid(row="6", column="1", padx=3, pady=3)
        txt_calendar_gs.grid(row="7", column="0", padx=3, pady=3, sticky='we')
        calendar_update_gs.grid(row="7", column="1", padx=3, pady=3)
        button_update_gs.grid(row="8", column="1", padx=3, pady=3)
        ### ----------------------------------------------------------------------------------------
        ### Раздел проверки расписания софта и ТМСа
        txt_title_check_schedule = ttk.Label(self,
                                             text="Проверка Опубликованных сеансов и расписания в TMS RB")
        txt_calendar_check_schedule = ttk.Label(self, text="Выберите дату для проверки расписания")
        calendar_check_schedule = DateEntry(self, date_pattern="YYYY-mm-dd")
        button_check_schedule = ttk.Button(self, text="Запустить проверку")

        txt_title_check_schedule.grid(row="9", column="1", padx=3, pady=3)
        txt_calendar_check_schedule.grid(row="10", column="0", padx=3, pady=3, sticky='we')
        calendar_check_schedule.grid(row="10", column="1", padx=3, pady=3)
        button_check_schedule.grid(row="11", column="1", padx=3, pady=3)





# Создаем виджет Treeview (аналог таблицы)

root = App()
root.mainloop()
