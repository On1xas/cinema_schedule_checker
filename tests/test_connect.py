from pythonping import ping
import colorama

network_data = {'PALAZZO': '172.20.21.1', 'ARENA': '172.20.22.1', 'DANA': '172.20.23.1', 'TRINITI': '172.20.24.1',
                'INTERNET': '8.8.8.8'}


def check_connection(thearte_name, ip):
    colorama.init()
    check_ping = ping(ip, verbose=False, count=1)
    if check_ping.stats_packets_returned == 1:
        print(f'Сетевое подключение к {thearte_name} - {colorama.Fore.GREEN}OK {colorama.Style.RESET_ALL}')
    else:
        print(f'Сетевое подключение к {thearte_name} - {colorama.Fore.RED}BAD {colorama.Style.RESET_ALL}')
        #raise ConnectionError(f'Проверьте сетевое подключение к {key}')


for key, value in network_data.items():
    check_connection(key, value)
