import tkinter
from tkinter import *
from tkinter import ttk
def get_connect():
    userlogin=username.get()
    userpassword=password.get()
    if userlogin:
        print(userlogin)
    else:
        print('LoginEmpty')
    if userpassword:
        print(userpassword)
    username.delete(0,tkinter.END)
    password.delete(0,tkinter.END)

window=Tk()
window.geometry('300x100')
window.title('Вход в приложение')
window.resizable(False,False)
window.iconbitmap()
tkinter.Label(window, text='Вход в систему').grid(row=0,column=1,sticky='w')
tkinter.Label(window, text='Login').grid(row=1,column=0,sticky='w')
username=tkinter.Entry(window)
username.grid(row=1,column=1)
tkinter.Label(window, text='Password').grid(row=2,column=0,sticky='w')
password=tkinter.Entry(window, show='*')
password.grid(row=2,column=1)
ttk.Button(window,text='Login', command=get_connect).grid(row=3,column=1, sticky='we')
window.grid_columnconfigure(0,minsize=100)
window.grid_columnconfigure(1,minsize=100)
window.grid_columnconfigure(2,minsize=100)
window.mainloop()