# pip install requests lxml, datetime, sqlite3, os, selenium, shutil, openpyxl
import os
import sqlite3
from config.config import project_path
# Создаем базу данных database.db в папке data
connect = sqlite3.connect(f'data\database.db')
cur = connect.cursor()
for i in range(1, 7):
    # Создаем таблицы залов кинотеатра ARENA_API
    sql = f'''CREATE TABLE IF NOT EXISTS ARENA_{i}_ROOM_API (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        TH_NAME TEXT,
        ROOM TEXT,
        SHOW_NAME TEXT,
        SHOW_TIME TEXT,
        FORMAT TEXT,
        AUDIO TEXT)'''
    cur.execute(sql)
    connect.commit()

for i in range(1, 8):
    # Создаем таблицы залов кинотеатра DANA_API
    sql = f'''CREATE TABLE IF NOT EXISTS DANA_{i}_ROOM_API (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        TH_NAME TEXT,
        ROOM TEXT,
        SHOW_NAME TEXT,
        SHOW_TIME TEXT,
        FORMAT TEXT,
        AUDIO TEXT)'''
    cur.execute(sql)
    connect.commit()
for i in range(1, 8):
    # Создаем таблицы залов кинотеатра PALAZZO_API
    sql = f'''CREATE TABLE IF NOT EXISTS PALAZZO_{i}_ROOM_API (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        TH_NAME TEXT,
        ROOM TEXT,
        SHOW_NAME TEXT,
        SHOW_TIME TEXT,
        FORMAT TEXT,
        AUDIO TEXT)'''
    cur.execute(sql)
    connect.commit()
for i in range(1, 6):
    # Создаем таблицы залов кинотеатра TRINITI_API
    sql = f'''CREATE TABLE IF NOT EXISTS TRINITI_{i}_ROOM_API (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        TH_NAME TEXT,
        ROOM TEXT,
        SHOW_NAME TEXT,
        SHOW_TIME TEXT,
        FORMAT TEXT,
        AUDIO TEXT)'''
    cur.execute(sql)
    connect.commit()

for i in range(1, 7):
    # Создаем таблицы залов кинотеатра ARENA_TMS , , , SPL_TITLE, CPL_TITLE
    sql = f'''CREATE TABLE IF NOT EXISTS ARENA_{i}_ROOM_TMS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        TH_NAME TEXT,
        ROOM TEXT,
        SHOW_START TEXT,
        SPL_TITLE TEXT,
        CPL_TITLE TEXT)'''
    cur.execute(sql)
    connect.commit()

for i in range(1, 8):
    # Создаем таблицы залов кинотеатра DANA_TMS
    sql = f'''CREATE TABLE IF NOT EXISTS DANA_{i}_ROOM_TMS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        TH_NAME TEXT,
        ROOM TEXT,
        SHOW_START TEXT,
        SPL_TITLE TEXT,
        CPL_TITLE TEXT)'''
    cur.execute(sql)
    connect.commit()
for i in range(1, 8):
    # Создаем таблицы залов кинотеатра PALAZZO_TMS
    sql = f'''CREATE TABLE IF NOT EXISTS PALAZZO_{i}_ROOM_TMS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        TH_NAME TEXT,
        ROOM TEXT,
        SHOW_START TEXT,
        SPL_TITLE TEXT,
        CPL_TITLE TEXT)'''
    cur.execute(sql)
    connect.commit()
for i in range(1, 6):
    # Создаем таблицы залов кинотеатра TRINITI_TMS
    sql = f'''CREATE TABLE IF NOT EXISTS TRINITI_{i}_ROOM_TMS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        TH_NAME TEXT,
        ROOM TEXT,
        SHOW_START TEXT,
        SPL_TITLE TEXT,
        CPL_TITLE TEXT)'''
    cur.execute(sql)
    connect.commit()
# Сводная таблица названий для проверки соответствия
sql = f'''CREATE TABLE IF NOT EXISTS PIVOT_SHOW_TABLE (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    SHOW_NAME_API TEXT,
    SPL_TITLE_NAME TEXT,
    LAST_UPDATE TEXT
    )'''
cur.execute(sql)
connect.commit()
connect.close()

with open('run-script.bat', 'w') as file:
    file.write('@echo off\n')
    directory=os.getcwd()
    file.write(f'{directory[0:2]}\n')
    file.write(f'cd {directory[3:]}\n')
    file.write('python main.py\n')
    file.write('@pause\n')

print('setup is Done!')