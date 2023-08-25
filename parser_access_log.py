import os
import re
import json


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
        regex = re.compile(
            '(?P<ip>.*?) - - (?P<date_time>.*? *]) "(?P<metod>.*?) (?P<content>.*?") (?P<code>[0-9]{3}) (?P<server_byte>.*) "(?P<url>.*?)" (?P<user_agent>.*) (?P<duration>.*)')
        if request_count > 3000000:
            # Извлечение HTTP-метода
            metod_line = regex.search(line).group('metod')
        metod_line = "GET"
        if metod_line in http_methods:
            http_methods[metod_line] += 1
        else:
            http_methods[metod_line] = 1
        # Извлечение IP адреса
        ip_line = regex.search(line).group('ip')
        if ip_line in ip_addresses:
            ip_addresses[ip_line] += 1
        else:
            ip_addresses[ip_line] = 1
        # длительность запроса
        duration_line = regex.search(line).group('duration')
        # url
        url_line = regex.search(line).group('url')
        # время запроса
        date_time_line = regex.search(line).group('date_time')
        request_info = {
            "method": metod_line,
            "url": url_line,
            "ip": ip_line,
            "duration(ms)": duration_line,
            "timestamp": date_time_line
        }
        # Добавление запроса в список самых долгих запросов
        longest_requests.append(request_info)
    log.close()
    # Сортировка самых долгих запросов по длительности
    longest_requests.sort(key=lambda x: int(x["duration(ms)"]), reverse=True)
    # Формирование статистики в виде словаря
    statistics = {
        "total_requests": request_count,
        "http_methods": http_methods,
        "top_ip_addresses": dict(sorted(ip_addresses.items(), key=lambda x: x[1], reverse=True)[:3]),
        "longest_requests": longest_requests[:3]
    }
    print(json.dumps(statistics, indent=4))
    # Сохранение статистики в json файл
    output_file = log_file + '.json'
    with open(output_file, 'w') as file:
        json.dump(statistics, file, indent=4)


# передача нужного файла и каталога
def analyze_logs(directory):
    for file in os.listdir(directory):
        # вывод в консоль
        print(f'*** Статистика из лога  "{file}" ***')
        if file.startswith("access"):
            if file.endswith(".log"):
                file_path = os.path.join(directory, file)
                analyze_log_file(file_path)


# Передача каталога, заменю потом на input
log_directory = 'C:\\access_test'
analyze_logs(log_directory)
