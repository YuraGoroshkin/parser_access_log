# parser_access_log
homework_28 OTUS

## Как работает скрипт:


- Запускаем parser_access_log.py
- Указываем каталог откуда требуется обработать access логи (в названии таких логов, должно быть слово access)
>Пример - C:\access_test или /home/ubuntu
- В месте где лежат логи access будут созданы файлы со статистикой с названием файла и расширением .json
- Так же статистика будет выведена в консоль

## Задание
```sh
Написать скрипт анализа приложенного access.log файла
Формат записи в файле лога:
%h %t "%r" %>s %b "%{Referer}i" "%{User-Agent}i" %D
%h - имя удаленного хоста
%t - время получения запроса
%r - тип запроса, его содержимое и версия
%s - код состояния HTTP
%b - количество отданных сервером байт
%{Referer} - URL-источник запроса
%{User-Agent} - HTTP-заголовок, содержащий информацию о запросе
%D - длительность запроса в миллисекундах
```

| Требования к реализации |
| ------ |
| 1) Должна быть возможность указать директорий где искать логи или конкретный файл |
| 2) Должна быть возможность обработки всех логов внутри одного директория |
| 3) Для access.log должна собираться следующая информация:общее количество выполненных запросов количество запросов по HTTP-методам: GET - 20, POST - 10 и т.п. (список необходимых методов можно посмотреть в RFC: https://datatracker.ietf.org/doc/html/rfc7231#section-4 и https://datatracker.ietf.org/doc/html/rfc5789#section-2)|
| 4) топ 3 IP адресов, с которых были сделаны запросы |
| 5) топ 3 самых долгих запросов, должно быть видно метод, url, ip, длительность, дату и время запроса|
| 6) Собранная статистика должна быть сохранена в json файл и выведена в терминал в свободном (но понятном!) формате|
|  7) Должен быть README.md файл, который описывает как работает скрипт                      |