import os
parsing_url_api='https://soft.silverscreen.by:8443/wssite/webapi/xml?mode=showtimes&date='
parsing_url_arena='http://172.20.22.1:9090'
parsing_url_dana='http://172.20.23.1:9090'
parsing_url_palazzo='http://172.20.21.1:9090'
parsing_url_triniti='http://172.20.24.1:9090'
tms_password='Limon4ik'
path_to_download=f'{os.getenv("USERPROFILE")}\Downloads'
source_path_arena=f'{path_to_download}\Schedule - BY_SS_ArenaCity.xlsx'
source_path_dana=f'{path_to_download}\Schedule - BY_SS_Dana.xlsx'
source_path_palazzo=f'{path_to_download}\Schedule - BY_SS_Palazzo.xlsx'
source_path_triniti=f'{path_to_download}\Schedule - BY_SS_GrodnoTrinity.xlsx'
project_path=os.path.abspath("main.py")[:-8]
destination_path = f'{project_path}\data'
theatre_names = ['mooon в ТРЦ Palazzo', 'Silver Screen в ТРЦ Arena city', 'mooon в ТРЦ Dana Mall', 'mooon в ТРК Triniti']
room_names = [['Зал 1 mooon IMAX', 'Зал 2 Vegas', 'Зал 3 VIP', 'Зал 4 Resto', 'Зал 5 mooon+  ', 'Зал 6 Kids',
         'Зал 7 Visa Premiere'],
        ['Зал 1', 'Зал 2', 'Зал 3', 'Зал 4', 'Зал 5', 'Зал 6'],
        ['Зал 1 Premiere', 'Зал 2', 'Зал 3 Screen X', 'Зал 4 Vegas lounge', 'Зал 5', 'Зал 6 VIP', 'Зал 7 VIP'],
        ['Зал 1', 'Зал 2 Lounge', 'Зал 3 Premiere', 'Зал 4 Resto', 'Зал 5 VIP']]
table_th_names = ['PALAZZO', 'ARENA', 'DANA', 'TRINITI']