from parsing.parse_cinema_api import *
import gspread
import time
gs = gspread.service_account(filename='gs_credentials.json')  # подключаем файл с ключами и пр.
sh = gs.open_by_key('17C7Ch7S9a3vHUIW3B8wGl7b_OYk9MuBRcssG6rbAGVQ')  # подключаем таблицу по ID
worksheet = sh.sheet1  # получаем первый лист
res=worksheet.get_all_records()

for item in parse_schedule_api():
    print(item)
    worksheet.append_row(item)

time.sleep(5)
print(len(worksheet.col_values(1)))
for row in range(0, len(worksheet.col_values(1))):
    worksheet.delete_rows(1)