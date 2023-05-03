import sqlite3
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry, Calendar
from application.app_func import update_pivot_raw, clear_table, load_table_info, delete_select_raw, start_parse
from parsing.schedule_googl_sheet import add_show_gsdb

Param = dict()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Тут будет название приложения')
        self.iconbitmap()
        self.minsize(1200, 800)
        f_c = Frame_control(self).place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
        f_t = Frame_table(self).place(relx=0, rely=0, relwidth=0.5, relheight=1)


class User(App):

    @staticmethod
    def clear_data_in_db():
        update_pivot_raw(Param["new_spl"], Param["id"])
        clear_table(Param['main_table'])
        load_table_info(Param['main_table'])


class Frame_table(tk.Frame, User):

    def __init__(self, window):
        super().__init__(window)
        self['background'] = 'yellow'
        self.table = ttk.Treeview(self, show='headings')
        Param['main_table'] = self.table
        self.put_widgets()
    def popup(self,event):
        item=self.table.selection()
        row=self.table.item(item)
        if row['values'] !="":
            self.menu.post(event.x_root, event.y_root)

    def put_widgets(self):
        #     # Задаем название стобцов
        heads = ['id', 'SHOW_NAME', 'SPL_TITLE']
        #     # Присватваем параметру "colums" название столбцов
        self.table['columns'] = heads
        #     # Передаем данные в таблицу. Вносим заголовки столбцов и выравниваем их по центру
        for head in heads:
            self.table.heading(head, text=head, anchor='center')
            # Передаем команду что данные в ячейках столбцов должна быть поцентру
            self.table.column(head, anchor='center')

        load_table_info(self.table)
        #
        scr_panel = ttk.Scrollbar(self)
        scr_panel.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.configure(yscrollcommand=scr_panel.set)
        self.table.pack(expand=tk.YES, fill=tk.BOTH, anchor='w')
        self.table.bind("<Button-3>", self.popup)
        self.menu = tk.Menu(tearoff=0)
        self.menu.add_command(label="Изменить SPL_TITLE", command=Change_spl_title_window)
        self.menu.add_command(label="Удалить", command=self.button_delete_raw)

    #
    def button_delete_raw(self):
        delete_select_raw(Param['main_table'])

class Frame_control(tk.Frame, User):

    def __init__(self, window):
        super().__init__(window)
        # self.put_widgets()

    # def put_widgets(self):
        # self.txt_title_spl_update = ttk.Label(self, text="Обновление данных в таблице")
        # self.txt_entry_id = ttk.Label(self, text="Введите ID сеанса")
        # self.txt_entry_new_spl_name = ttk.Label(self, text="Введите новое название SPL")
        # self.entry_id_label = ttk.Entry(self)
        # self.entry_new_spl_name = ttk.Entry(self)
        # self.button_id = ttk.Button(self, text='Обновить данные в БД', command=)
        #
        # self.txt_title_spl_update.grid(row="0", column="1", padx=3, pady=3)
        # self.txt_entry_id.grid(row="1", column="0", padx=3, pady=3)
        # self.txt_entry_new_spl_name.grid(row="2", column="0", padx=3, pady=3)
        # self.entry_id_label.grid(row='1', column='1')
        # self.entry_new_spl_name.grid(row='2', column='1')
        # self.button_id.grid(row="3", column="1", padx=3, pady=3, sticky="s")

        # self.txt_title_button_clear_raw = ttk.Label(self,
        #                                             text="Если прокат фильма закончился \n Выберите в таблице строку для удаления")
        # self.button_id = ttk.Button(self, text='Удалить строку', command=self.button_delete_raw)
        # self.txt_title_button_clear_raw.grid(row="4", column="1", padx=3, pady=3)
        # self.button_id.grid(row="5", column="1", padx=3, pady=3)

    # def button_delete_raw(self):
    #     return delete_select_raw(Param['main_table'])

    #     ### ----------------------------------------------------------------------------------------

    #     ### ----------------------------------------------------------------------------------------
    #     ### Раздел ОБНОВЛЕНИЯ ГУГЛ ТАБЛИЦЫ ЧБОБО
        txt_title_update_gs = ttk.Label(self, text="Обновленние ВЫГРУЗКИ в таблице расписания чбобо")
        txt_calendar_gs = ttk.Label(self, text="\tВыберите дату \n \tдля выгрузки данных")
        self.calendar_update_gs = DateEntry(self, date_pattern="YYYY-mm-dd")
        button_update_gs = ttk.Button(self, text="Обновить таблицу", command=lambda : add_show_gsdb(self.calendar_update_gs.get_date()))

        txt_title_update_gs.grid(row="6", column="1", padx=3, pady=3)
        txt_calendar_gs.grid(row="7", column="0", padx=3, pady=3, sticky='we')
        self.calendar_update_gs.grid(row="7", column="1", padx=3, pady=3)
        button_update_gs.grid(row="8", column="1", padx=3, pady=3)
    #     ### ----------------------------------------------------------------------------------------
    #     ### Раздел проверки расписания софта и ТМСа
        txt_title_check_schedule = ttk.Label(self,
                                             text="Проверка Опубликованных сеансов и расписания в TMS RB")
        txt_calendar_check_schedule = ttk.Label(self, text="Выберите дату для проверки расписания")
        self.calendar_check_schedule = DateEntry(self, date_pattern="YYYY-mm-dd")
        button_check_schedule = ttk.Button(self, text="Запустить проверку", command=lambda : start_parse(str(self.calendar_check_schedule.get_date())))

        txt_title_check_schedule.grid(row="9", column="1", padx=3, pady=3)
        txt_calendar_check_schedule.grid(row="10", column="0", padx=3, pady=3, sticky='we')
        self.calendar_check_schedule.grid(row="10", column="1", padx=3, pady=3)
        button_check_schedule.grid(row="11", column="1", padx=3, pady=3)

# Создаем виджет Treeview (аналог таблицы)
class Change_spl_title_window(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Тут будет название приложения')
        self.iconbitmap()
        self.minsize(150, 120)
        tk.Frame(self)
        self.put_widjet()
    def put_widjet(self):
        self.txt_title_spl_update = ttk.Label(self, text="Обновление данных в таблице")
        self.txt_entry_id = ttk.Label(self, text="Введите ID сеанса")
        self.txt_entry_new_spl_name = ttk.Label(self, text="Введите новое название SPL")
        self.entry_id_label = ttk.Entry(self)
        self.entry_new_spl_name = ttk.Entry(self)
        self.button_id = ttk.Button(self, text='Обновить данные в БД', command=self.button_get_id)

        self.txt_title_spl_update.grid(row="0", column="1", padx=3, pady=3)
        self.txt_entry_id.grid(row="1", column="0", padx=3, pady=3)
        self.txt_entry_new_spl_name.grid(row="2", column="0", padx=3, pady=3)
        self.entry_id_label.grid(row='1', column='1')
        self.entry_new_spl_name.grid(row='2', column='1')
        self.button_id.grid(row="3", column="1", padx=3, pady=3, sticky="s")
        self.entry_id_label.insert(0, self.request_id())

    def request_id(self):
        item = Param['main_table'].selection()
        p_id = Param['main_table'].item(item)
        print(p_id['values'][0])
        return str(p_id['values'][0])
    def button_get_id(self):

        Param["id"] = self.entry_id_label.get()
        Param["new_spl"] = self.entry_new_spl_name.get()
        self.entry_id_label.delete(0, tk.END)
        self.entry_new_spl_name.delete(0, tk.END)
        User.clear_data_in_db()
        self.destroy()

window = App()

window.mainloop()
