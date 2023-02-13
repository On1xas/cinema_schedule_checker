cinema_schedule_checker
Цель проекта - оптимизация рабочего процесса киномехаников по проверке расписания киносеансов в киносети.

Вводное техническое задание:

Краткое описание проекта:

По API из программного обеспечения букера, через GET запрос получаем HTML ответ, в котором в формате XML расписаны все опубликованные киносеансы. При помощи Selenium подключаемся поочередно на каждый TMS Rosetta Bridge сервер, скачиваем XLSM таблицу с подготовленным расписанием. Сведение полученной информации в базу данных для дальнейшей обработки. Производим сверку расписаний между API букера и TMS.

Путевой лист проекта: 11.02.23 - создание проекта,формирование первичной структуры, подготовка github репозитория, скачивание необходимых библиотек, хромдрайвера. 02.2:

Подготовить парсиг API програмного обеспечения букера
Подготовить парсинг TMS серверов
Подключить базу данных Sqlite3
Контроль версий: 0.1 -

Установка: Переносим проект в корень диска C:\ рабочего компьютера киномехаников.