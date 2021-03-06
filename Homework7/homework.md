## Домашнее задание по блоку Docker + Docker-compose

## Срок выполнения ДЗ -  16.11.21 21:00 !

### 1. Декодер.

Требуется выкачать образ из Container registry (Gitlab):

```
gitlab-registry.ozon.dev/qa/teachers/qa-route-256
```

Внутри образа находится python-скрипт, который принимает на вход аргумент ```--decode``` (библиотека ```argparse```).
Ваша задача - передать на вход контейнеру следующую закодированную строку:

```
Q29uZ3JhdHVsYXRpb25zISBGaXJzdCBkb2NrZXIgaG9tZXdvcmsgaXMgc3VjY
```
Решением задания будет считаться раскодированная строка, которую необходимо прислать тьютору.

### 2. Локальная база данных для стены сообщений.

В директории ```compose/homeworks/second``` находится Flask-приложение ```app.py```.
При старте оно поднимает веб-сервер с примером стены сообщений, в котором доступны две страницы:

* / 
* /comments 

```index.html```- стартовая страница: для ввода имени и комментария.

```comments.html```- страница для отображения результатов.

HTML-файлы доступны в директории ```./templates```.

Сейчас введенные в форму данные нигде не сохраняются - на странице ```/comments``` отображается хардкод:

```note
25     example = [Comment('asvezh', 'random text')]
```

Задание:
1. Докеризовать приложение.
2. Доработать приложение так, чтобы данные, введенные в форму, отображались на странице ```/commemts```

При рестарте контейнера данные должны сохраняться!

Можно выбрать базу для хранения из следущего списка: 

```
sqlite3
mysql 
postgresql
``` 

3. Задание принимается в формате образа, загруженного в Container Registry (Gitlab), с тегом ```homework```:

```
gitlab-registry.ozon.dev/<users>/qa-route-256:homework
```

### 3. Docker-compose для стены сообщений. (опционально!)

Для того же приложения (```compose/homeworks/second```) так же требуется добавить сохранение данных.

Условия:
1. Теперь база должна быть развернута в отдельном контейнере.
2. Приложение должно подниматься с помощью ```docker-compose```.
3. Данные, введенные в форму, должны сохраняться в БД и отображаться на странице ```/commemts```
4. Задание принимается в виде МР в вашем форк-репозитории (по аналогии с предыдущими ДЗ).

Базу по-прежнему можно выбрать самостоятельно из списка.


