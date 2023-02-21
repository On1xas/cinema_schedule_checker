import shutil
import time
import os
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from config.config import parsing_url_arena, source_path_arena, path_to_download, project_path
import sqlite3


def parser_tms_arena():
    driver = webdriver.Chrome()
    driver.get(parsing_url_arena)  # Подключаемся на TMS ArenaCity
    driver.maximize_window()
    time.sleep(3)
    element = driver.find_element(By.XPATH,
                                  '//*[@id="tms-view-body"]/div/div/div[3]/div[2]/div[2]/form/div[1]/input[2]')
    element.send_keys("Limon4ik")
    driver.find_element(By.XPATH, '//*[@id="tms-view-body"]/div/div/div[3]/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH,
                        '/html/body/tms/div/div[5]/header/div[5]/tms-navigation-header-menu/div[4]/div/div[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,
                        '//*[@id="tms-view-body"]/tms-schedule-builder/div/div/tms-date-range-picker/div/button[2]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,
                        '//*[@id="tms-view-body"]/tms-schedule-builder/div/div/tms-export-button/tms-dropdown-actions/tms-dropdown/button/i').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        '//*[@id="tms-view-body"]/tms-schedule-builder/div/div/tms-export-button/tms-dropdown-actions/tms-dropdown/div/div/tms-list-select/div[1]/tms-list-select-item[3]/div/span').click()
    time.sleep(1)
    driver.close()
    driver.quit()
    # path_to_download = r'C:\Users\e.aleynikov\Downloads'
    os.chdir(path_to_download)
    # source_path_arena = r'C:\Users\e.aleynikov\Downloads\Schedule - BY_SS_ArenaCity.xlsx'

    if os.path.exists(source_path_arena):
        destination_path = fr'{project_path}\data'
        shutil.move(source_path_arena, destination_path)
    time.sleep(1)

    wookbook = openpyxl.load_workbook(fr'{project_path}\data\Schedule - BY_SS_ArenaCity.xlsx')
    worksheet = wookbook.active
    data = []
    for i in range(1, worksheet.max_row):
        temp = []
        for col in worksheet.iter_cols(1, worksheet.max_column - 2):
            temp.append(col[i].value)
        del temp[2], temp[2], temp[2], temp[2], temp[2]
        data.append(tuple(temp))
    return data
