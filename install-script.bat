@echo off
pip install requests
pip install openpyxl
pip install shutil
pip install selenium
pip install colorama
pip install lxml
#choco install git
D:
mkdir D:\CinemaChecker
cd D:\CinemaChecker
git init
git clone https://github.com/On1xas/cinema_schedule_checker.git
cd D:\CinemaChecker\cinema_schedule_checker
python setup.py
@pause