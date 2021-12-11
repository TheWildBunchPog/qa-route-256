1. Самый взрослый пользователь.
Дана таблица:
CREATE TABLE users
(
    id   serial,
    name varchar(40),
    age  integer
);
Напишите запрос, который покажет имя самого взрослого пользователя в таблице

SELECT name FROM users ORDER BY age DESC LIMIT 1;


2. Где пользователи?
Даны связанные таблицы таблицы:
CREATE TABLE users
(
    id          serial primary key,
    name        varchar(40),
    location_id integer not null references location (id)
);
CREATE TABLE location
(
    id          serial primary key,
    name        varchar(40)
);
Напишите запрос, который покажет 10 имен пользователей, которыйе живут в Москве

SELECT users.name FROM users 
JOIN location on users.location_id = location.id 
WHERE location.name='Moscow'
LIMIT 10;
