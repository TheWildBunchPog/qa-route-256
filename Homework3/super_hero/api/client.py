from urllib.parse import urljoin
import requests


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:
    def __init__(self):
        self.base_url = 'https://superheroapi.com/'
        self.token = 632616764568400
        self.session = requests.Session()

    def _request(self, method, location, headers=None, data=None, expected_status=200):

        url = urljoin(self.base_url, location)

        response = self.session.request(method, url, headers=headers, data=data)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f' Got {response.status_code} {response.reason} for URL "{url}"')

        return response

    def get_information_of_hero(self, hero_id):

        location = f'api/{self.token}/{hero_id}'

        response = self._request('GET', location)
        return response

    def get_ids_of_heroes(self):

        location = 'ids.html'

        response = self._request('GET', location)
        return response

    def get_power_stats(self, hero_id):

        location = f'api/{self.token}/{hero_id}/powerstats'

        response = self._request('GET', location)
        return response
