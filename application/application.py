import tkinter as tk
from tkinter import ttk
from app_func import *
def clear_data_in_db():
    new_id=entry_id_label.get()
    new_spl=entry_new_spl_name.get()
    update_pivot_raw(new_spl,new_id)
    clear_table(table)
    load_table_info(table)
    entry_id_label.delete(0,tk.END)
    entry_new_spl_name.delete(0,tk.END)

def delete_raw():
    delete_select_raw(table)

window = tk.Tk()
window.title('Тут будет название приложения')
window.iconbitmap()
window.minsize(1200, 800)
frame_table = tk.Frame(window)
frame_control = tk.Frame(window)

frame_table.place(relx=0, rely=0, relwidth=0.5, relheight=1)
frame_control.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

tmp_data=[(3, ' Аватар: Путь воды ', 'BLUEWATERPEOPL', '2023-02-24 14:51:52.778549'), (6, ' Непослушная ', 'Naughty', '2023-02-24 14:51:52.760532'), (13, ' Чебурашка ', 'CHEBURASHKA', '2023-02-24 14:51:52.789106'), (19, ' Топ Ган: Мэверик ', 'TOPGUNMAVERICK', '2023-02-24 14:51:52.766551'), (22, ' Свободные отношения ', 'SVO', '2023-02-22 14:47:05.328507'), (23, ' Элвис ', 'Elvis', '2023-02-22 14:47:05.331517'), (24, ' Знакомство родителей ', 'MaybeIDo', '2023-02-22 14:47:05.344560'), (25, ' Кот в сапогах 2: Последнее желание ', 'PiBLastWish', '2023-02-24 14:51:52.784184'), (26, ' Астерикс и Обеликс: Поднебесная ', 'ASTERIXEMPIRE', '2023-02-24 14:51:52.786829'), (27, ' Заклятье. Первое причастие ', 'TheCommunion', '2023-02-24 14:51:52.806131'), (28, ' Амстердам ', 'Amsterdam', '2023-02-22 14:47:05.338541'), (29, ' Мой домашний крокодил ', 'LYLELYLECROCODILE', '2023-02-22 14:47:05.347572'), (33, ' Одиноки вместе ', 'AloneTogether', '2023-02-22 14:47:05.317470'), (34, ' Изумительный Морис ', 'AmazingMaurice', '2023-02-22 14:47:05.320482'), (35, ' Легион супергероев ', 'Legion', '2023-02-22 11:26:50.188535'), (36, ' Предпоказ. Рок Дог 3: Битва за бит ', 'RockDog3', '2023-02-22 14:47:05.364818'), (37, ' Кто украл Banksy (RU SUB) ', 'ManStoleBanksy', '2023-02-22 14:47:05.325497'), (38, ' Снежная королева: Разморозка ', 'SQ', '2023-02-24 14:51:52.799809'), (39, ' Спецпоказ. Сын ', 'TheSon', '2023-02-23 17:22:47.379858'), (40, ' Марлоу ', 'MARLOU', '2023-02-24 14:51:52.802818'), (41, ' TheatreHD: Курентзис: Бетховен Симфония № 9 ', 'BETH', '2023-02-23 17:22:47.366008'), (42, ' Italian Best Shorts 5: Жизнь как чудо ', 'ItBest', '2023-02-24 14:51:52.757521'), (43, ' Рок дог 3: Битва за бит ', 'RockDog3', '2023-02-24 14:51:52.775559'), (44, ' Мумиёшки ', 'a', '2023-02-24 14:51:52.781176'), (45, ' Бешенство ', 'RAGE', '2023-02-24 14:51:52.797804'), (46, ' Папы против мам ', 'fas', '2023-02-24 14:51:52.763542'), (47, ' Сын ', 'd', '2023-02-24 14:51:52.769561'), (48, ' Титаник (Перевыпуск) ', 'sdf', '2023-02-24 14:51:52.772571'), (49, ' TheatreHD: Роден ', 's', '2023-02-24 14:51:52.792114'), (50, ' Музыкотерапия. Источник ', 'f', '2023-02-24 14:51:52.794848')]

# Создаем виджет Treeview (аналог таблицы)
table=ttk.Treeview(frame_table, show='headings')

# Задаем название стобцов
heads=['id', 'SHOW_NAME', 'SPL_TITLE']
# Присватваем параметру "colums" название столбцов
table['columns']=heads

# Передаем данные в таблицу. Вносим заголовки столбцов и выравниваем их по центру
for head in heads:
    table.heading(head, text=head, anchor='center')
    # Передаем команду что данные в ячейках столбцов должна быть поцентру
    table.column(head,  anchor='center')

load_table_info(table)

scr_panel=ttk.Scrollbar(frame_table, command=table.yview)
scr_panel.pack(side=tk.RIGHT, fill=tk.Y)
table.configure(yscrollcommand=scr_panel.set)
table.pack(expand=tk.YES, fill=tk.BOTH, anchor='w')

### БЛОК ИЗМЕНЕНИЯ НАЗВАНИЯ ПЛЕЙЛИСТА
### ----------------------------------------------------------------------------------------
txt_title_spl_update = ttk.Label(frame_control, text="Обновление данных в таблице")
txt_entry_id = ttk.Label(frame_control, text="Введите ID сеанса")
txt_entry_new_spl_name = ttk.Label(frame_control, text="Введите новое название SPL")
entry_id_label=ttk.Entry(frame_control)
entry_new_spl_name=ttk.Entry(frame_control)
button_id = ttk.Button(frame_control, text='Обновить данные в БД', command=clear_data_in_db)

txt_title_spl_update.grid(row="0", column="1",padx=3,pady=3)
txt_entry_id.grid(row="1", column="0" ,padx=3,pady=3)
txt_entry_new_spl_name.grid(row="2", column="0" ,padx=3,pady=3)
entry_id_label.grid(row='1', column='1')
entry_new_spl_name.grid(row='2', column='1')
button_id.grid(row="3", column="1" ,padx=3,pady=3)
### ----------------------------------------------------------------------------------------
txt_title_button_clear_raw = ttk.Label(frame_control, text="Выберите строку для удаления")
button_id = ttk.Button(frame_control, text='Удалить строку', command=delete_raw)

txt_title_button_clear_raw.grid(row="4", column="1" ,padx=3,pady=3)
button_id.grid(row="5", column="1" ,padx=3,pady=3)


window.mainloop()
