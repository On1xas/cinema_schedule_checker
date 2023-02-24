import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title('Тут будет название приложения')
window.iconbitmap()

frame_table=tk.Frame(window,width=200,height=200, bg='yellow')
frame_control=tk.Frame(window,width=200,height=200, bg='green')

frame_table.grid(row=0,column=0)
frame_control.grid(row=0,column=1)


# heads=['id', 'SHOW_NAME', 'SPL_TITLE']
# table = ttk.Treeview(data_table)
# table['colums']=heads
# for header in heads:
#     table.heading(header, text=header, anchor='center')
#     table.column(header, anchor='center')
# for row in data_table:
#     table.insert("", tk.END, values=row)
#
# table.pack(expand=tk.YES, fill=tk.BOTH)




window.mainloop()