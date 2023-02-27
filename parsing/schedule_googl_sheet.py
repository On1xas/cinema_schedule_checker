from parsing.parse_cinema_api import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

gs = gspread.service_account(filename='gs_credentials.json')  # подключаем файл с ключами и пр.
sh = gs.open_by_key('17C7Ch7S9a3vHUIW3B8wGl7b_OYk9MuBRcssG6rbAGVQ')  # подключаем таблицу по ID
worksheet = sh.sheet1  # получаем первый лист
res=worksheet.get_all_records()
worksheet.