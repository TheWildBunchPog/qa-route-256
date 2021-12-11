from urllib.parse import urljoin
import requests


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:
    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com/'

    def _request(self, method, location, headers=None, data=None):

        url = urljoin(self.base_url, location)

        response = requests.request(method, url, headers=headers, data=data)

        # if response.status_code != expected_status:
        #     raise ResponseStatusCodeException(f' Got {response.status_code} {response.reason} for URL "{url}"')

        return response

    def get_information_of_users(self):

        location = 'users'

        response = self._request('GET', location)
        return response

    def get_information_of_user_posts(self, user_id):

        location = f'users/{user_id}/posts'

        response = self._request('GET', location)
        return response

    def get_information_of_user_albums(self, user_id):

        location = f'users/{user_id}/albums'

        response = self._request('GET', location)
        return response

    def get_information_of_user_todos(self, user_id):

        location = f'users/{user_id}/todos'

        response = self._request('GET', location)
        return response
