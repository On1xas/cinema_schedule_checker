import os
parsing_url_api='https://soft.silverscreen.by:8443/wssite/webapi/xml?mode=showtimes&date='
parsing_url_arena='http://172.20.22.1:9090'
parsing_url_dana='http://172.20.23.1:9090'
parsing_url_palazzo='http://172.20.21.1:9090'
parsing_url_triniti='http://172.20.24.1:9090'
tms_password='Limon4ik'
path_to_download=fr'{os.getenv("USERPROFILE")}\Downloads'
source_path_arena=fr'{path_to_download}\Schedule - BY_SS_ArenaCity.xlsx'
source_path_dana=fr'{path_to_download}\Schedule - BY_SS_Dana.xlsx'
source_path_palazzo=fr'{path_to_download}\Schedule - BY_SS_Palazzo.xlsx'
source_path_triniti=fr'{path_to_download}\Schedule - BY_SS_GrodnoTrinity.xlsx'
project_path=os.path.abspath("config.py")[:-17]
destination_path = fr'{project_path}\data'
