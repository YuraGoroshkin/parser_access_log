import os
import re


def analyze_log_file(log_file):
    # Словари для сбора статистики
    request_count = 0
    http_methods = {}
    ip_addresses = {}
    longest_requests = []
    log = open(log_file, 'r')
    while True:
        # считываем строку
        line = log.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        request_count += 1
        # регулярное выражение которое собрал https://regex101.com/r/4WTc1W/1
        regex = re.compile('(?P<ip>.*?) - - (?P<date_time>.*? *]) "(?P<metod>.*?) (?P<content>.*?") (?P<code>[0-9]{3}) (?P<server_byte>.*) (?P<url>.*?") (?P<user_agent>.*) (?P<duration>.*)')
        ip_line = regex.search(line).group('ip')
        print(ip_line)
    log.close()
    print(request_count)


# передача нужного файла и каталога
def analyze_logs(directory):
    for file in os.listdir(directory):
        # вот тут наверное стоит будет возвращать какую-то переменную, для названия обработанного файла
        print(file)
        if file.startswith("access"):
            if file.endswith(".log"):
                file_path = os.path.join(directory, file)
                analyze_log_file(file_path)


# Передача каталога, заменю потом на input
log_directory = 'C:\\access_test'
analyze_logs(log_directory)
