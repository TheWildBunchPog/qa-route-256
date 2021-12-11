import csv
import os
import xml.etree.ElementTree as xml

from loguru import logger

from api.api_client import ApiClient


logs_path = os.path.join(os.path.abspath(os.path.join(__file__, os.pardir)), 'logs/logs.log')
logger.add(logs_path, level='INFO')


class Parser:
    client = ApiClient()

    @staticmethod
    def read_email_list(file_path) -> list:
        """считываем emails из csv файла, возвращаем их списком"""
        with open(file_path) as f:
            reader = csv.reader(f)
            for row in reader:
                email_list = row

        logger.info(f'Количество пользователей для запуска - {len(email_list)}')
        return email_list

    def get_id_users(self, email_list_user) -> list:
        """сопоставляем email пользователя и id пользователя, возвращаем список связок {id: email}"""
        information_of_users = self.client.get_information_of_users()
        logger.info(f'Время получения информации о всех пользователях - {information_of_users.elapsed.total_seconds()} сек')
        users_list = information_of_users.json()

        id_and_email = []
        for email in email_list_user:
            for user in users_list:
                if email == user["email"]:
                    id_and_email.append({"id": user["id"], "email": email})

        if not id_and_email:
            logger.warning(f'Информация об пользователях {email_list_user} не найдена')

        logger.info(f'Количество пользователей, о которых найдена информация  - {len(id_and_email)}')
        return id_and_email

    def get_users_posts(self, user_id):
        """отправляем запрос на получение всех post пользователя, возвращаем их списком"""
        user_posts = self.client.get_information_of_user_posts(user_id)
        response_time = user_posts.elapsed.total_seconds()
        logger.info(f'Время получения информации о posts пользователя с id {user_id} - {response_time} сек')

        return user_posts

    def get_users_albums(self, user_id):
        """отправляем запрос на получение всех album пользователя, возвращаем их списком"""
        user_albums = self.client.get_information_of_user_albums(user_id)
        response_time = user_albums.elapsed.total_seconds()
        logger.info(f'Время получения информации о albums пользователя с id {user_id} - {response_time} сек')

        if user_albums.status_code == 400:
            logger.warning('Bad Request')

        return user_albums

    def get_users_todos(self, user_id):
        """отправляем запрос на получение всех to do пользователя, возвращаем их списком"""
        user_todos = self.client.get_information_of_user_todos(user_id)
        response_time = user_todos.elapsed.total_seconds()
        logger.info(f'Время получения информации о todos пользователя с id {user_id} - {response_time} сек')

        return user_todos

    def create_xml_with_information_about_user(self, id_and_email_of_users):
        """собираем и сохраняем xml файл для каждого пользователя"""

        users_information = []

        for user in id_and_email_of_users:

            logger.info(f'Starts parsing for {user["email"]}')

            user_posts = self.get_users_posts(user["id"]).json()
            user_albums = self.get_users_albums(user["id"]).json()
            user_todos = self.get_users_todos(user["id"]).json()

            root = xml.Element("user")
            user_id = xml.SubElement(root, "id")
            user_id.text = str(user['id'])

            user_email = xml.SubElement(root, "email")
            user_email.text = user['email']

            posts = xml.Element("posts")
            root.append(posts)

            # добавляем в элемент posts все post пользователя
            for user_post in user_posts:
                post = xml.Element("post")
                posts.append(post)

                post_id = xml.SubElement(post, "id")
                post_id.text = str(user_post['id'])

                post_title = xml.SubElement(post, "title")
                post_title.text = user_post['title']

                post_body = xml.SubElement(post, "body")
                post_body.text = user_post['body']

            albums = xml.Element("albums")
            root.append(albums)

            # добавляем в элемент albums все album пользователя
            for user_album in user_albums:
                album = xml.Element("album")
                albums.append(album)

                album_id = xml.SubElement(album, "id")
                album_id.text = str(user_album['id'])

                album_title = xml.SubElement(album, "title")
                album_title.text = user_album['title']

            todos = xml.Element("todos")
            root.append(todos)

            # добавляем в элемент todos все to do пользователя
            for user_todo in user_todos:
                todo = xml.Element("todo")
                todos.append(todo)

                todo_id = xml.SubElement(todo, "id")
                todo_id.text = str(user_todo['id'])

                todo_title = xml.SubElement(todo, "title")
                todo_title.text = user_todo['title']

                todo_completed = xml.SubElement(todo, "completed")
                todo_completed.text = str(user_todo['completed'])

            tree = xml.ElementTree(root)
            users_information.append(tree)

        return users_information

    @staticmethod
    def save_xml_with_information_about_user(information_of_users):
        """собираем и сохраняем xml файл для каждого пользователя"""

        for user in information_of_users:
            root = user.getroot()
            user_id = root[0].text

            users_path = os.path.join(os.path.abspath(os.path.join(__file__, os.pardir)), f'users/{user_id}.xml')
            with open(users_path, "wb") as fh:
                user.write(fh)


if __name__ == "__main__":
    data_path = os.path.join(os.path.abspath(os.path.join(__file__, os.pardir)), 'users/emails.csv')

    print(f"Передайте путь до файлы csv с emails (по умолчанию {data_path}):")
    to_file_path = input()

    if not to_file_path:
        to_file_path = data_path

    email_list = Parser().read_email_list(to_file_path)
    id_and_email = Parser().get_id_users(email_list)
    users_information = Parser().create_xml_with_information_about_user(id_and_email)
    Parser().save_xml_with_information_about_user(users_information)
