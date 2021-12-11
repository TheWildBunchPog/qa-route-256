import csv
import os
import random
import xml.etree.ElementTree as xml

import httpretty
from loguru import logger
import vcr

from parser import Parser
from api.api_client import ApiClient


class TestParser:
    parser = Parser()
    client = ApiClient()

    def test_read_email_list(self, mocker):
        """Тест работоспособности чтения csv файла
           Ожидаемый результат: emails до записи == emails после записи в csv и чтения через read_email_list"""
        test_emails = ['test1@mail.ru', 'test2@mail.ru, test3@mail.ru']
        email_list_path = 'test_read_email_list.csv'

        # мокаем логгер
        mocker.patch('parser.logger.info')

        # записываем список emails в тестовый файл csv
        with open(email_list_path, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(test_emails)

        # считываем тестовый файл csv с emails
        emails_result = self.parser.read_email_list(email_list_path)

        # удаляем тестовый файл csv с emails
        os.remove(email_list_path)

        logger.info.assert_called_once_with(f'Количество пользователей для запуска - {len(test_emails)}')
        assert test_emails == emails_result

    def test_get_users_posts(self, mocker, test_id=random.randint(1, 10)):
        """Тест получения данных о posts пользователя
           Ожидаемый результат: id на входе == id в ответе"""
        # мокаем логгер
        mocker.patch('parser.logger.info')

        response = self.parser.get_users_posts(test_id)
        response_time = response.elapsed.total_seconds()

        logger.info.assert_called_once_with(f'Время получения информации о posts пользователя с id {test_id} - {response_time} сек')
        assert test_id == response.json()[0]['userId']

    def test_get_users_albums(self, mocker, test_id=random.randint(1, 10)):
        """Тест получения данных о albums пользователя
           Ожидаемый результат: id на входе == id в ответе"""
        # мокаем логгер
        mocker.patch('parser.logger.info')

        response = self.parser.get_users_albums(test_id)
        response_time = response.elapsed.total_seconds()

        logger.info.assert_called_once_with(f'Время получения информации о albums пользователя с id {test_id} - {response_time} сек')
        assert test_id == response.json()[0]['userId']

    def test_get_users_todos(self, mocker, test_id=random.randint(1, 10)):
        """Тест получения данных о todos пользователя
           Ожидаемый результат: id на входе == id в ответе"""
        # мокаем логгер
        mocker.patch('parser.logger.info')

        response = self.parser.get_users_todos(test_id)
        response_time = response.elapsed.total_seconds()

        logger.info.assert_called_once_with(f'Время получения информации о todos пользователя с id {test_id} - {response_time} сек')
        assert test_id == response.json()[0]['userId']

    def test_get_id_users(self, mocker):
        """Тест получения данных о пользователях
           Ожидаемый результат: переданные валидные emails == emails после поиска пользователей"""
        # мокаем логгер
        mocker.patch('parser.logger.info')
        mocker.patch('parser.logger.warning')
        # мокаем загрузку файлов
        users = ['Sincere@april.biz', 'Lucio_Hettinger@annie.ca', 'Rey.Padberg@karina.biz']
        mocker.patch('parser.Parser.read_email_list', return_value=users)
        email_list_user = Parser().read_email_list('fake')
        id_and_emails = self.parser.get_id_users(email_list_user)

        emails = []
        for email in id_and_emails:
            emails.append(email['email'])

        Parser.read_email_list.assert_called_once_with('fake')
        assert users == emails

    def test_create_xml_with_information_about_user(self, mocker):
        """Тест создания xml файлов о пользователях
           Ожидаемый результат: переданные emails и id == emails и id после записи в xml"""
        # мокаем логгер
        mocker.patch('parser.logger.info')
        # мокаем получение id пользователей
        id_and_email = [{'id': 1, 'email': 'Sincere@april.biz'},
                        {'id': 5, 'email': 'Lucio_Hettinger@annie.ca'},
                        {'id': 10, 'email': 'Rey.Padberg@karina.biz'}]
        mocker.patch('parser.Parser.get_id_users', return_value=id_and_email)
        id_and_email_of_users = Parser().get_id_users('fake')
        users_information = self.parser.create_xml_with_information_about_user(id_and_email_of_users)

        id_and_email_result = []
        for user in users_information:
            root = user.getroot()
            id_and_email_result.append({"id": int(root[0].text), "email": root[1].text})

        Parser.get_id_users.assert_called_once_with('fake')
        assert id_and_email == id_and_email_result

    def test_save_xml_with_information_about_user(self, mocker):
        """Тест работоспособности сохранения xml файла
           Ожидаемый результат: emails до сохранения == emails после сохранения в xml"""
        # мокаем логгер
        mocker.patch('parser.logger.info')
        id_and_email = [{'id': 1, 'email': 'Sincere@april.biz'}]
        users_information = self.parser.create_xml_with_information_about_user(id_and_email)

        # мокаем os.path.join
        fake_file_path = 'fake_save.xml'
        mocker.patch('parser.os.path.join', return_value=fake_file_path)

        xml_file_path = self.parser.save_xml_with_information_about_user(users_information)

        # открываем ранее сохраненный файл xml и считываем id и email пользователя
        tree = xml.parse(fake_file_path)
        root = tree.getroot()
        id_and_email_xml = [{'id': int(root[0].text), 'email': root[1].text}]

        # удаляем тестовый файл xml с id и email пользователя
        os.remove(fake_file_path)

        assert id_and_email == id_and_email_xml

    @vcr.use_cassette
    def test_mock_mock_get_users_albums(self, mocker):
        """Тест мока http request,  хочу проверить, что выведится warning лог при коде ответа 400
           Ожидаемый результат: response status code == 400"""
        # мокаем логгер
        mocker.patch('parser.logger.info')
        mocker.patch('parser.logger.warning')

        user_id = 5
        response = self.parser.get_users_albums(user_id)
        response_time = response.elapsed.total_seconds()

        logger.info.assert_called_once_with(f'Время получения информации о albums пользователя с id {user_id} - {response_time} сек')
        logger.warning.assert_called_once_with('Bad Request')
        assert response.status_code == 400

    @httpretty.activate
    def test_mock_get_users_posts(self, mocker):
        """Тест мока http request, body response на который нам нужно
           Ожидаемый результат: response.json() == fake_body"""
        # мокаем логгер
        mocker.patch('parser.logger.info')

        user_id = random.randint(1, 10)
        url = f'https://jsonplaceholder.typicode.com/users/{user_id}/posts'
        httpretty.register_uri(httpretty.GET, url, body='{"fake": "body"}')

        response = self.parser.get_users_posts(user_id)
        response_time = response.elapsed.total_seconds()

        logger.info.assert_called_once_with(f'Время получения информации о posts пользователя с id {user_id} - {response_time} сек')
        assert response.json() == {"fake": "body"}
