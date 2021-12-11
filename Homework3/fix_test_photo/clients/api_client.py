import requests

from fix_test_photo.settings import URL, HEADERS


class ApiClient:

    def get_find_by_status(self, params, path="/v2/pet/findByStatus"):
        """

        :param params:
        :param path:
        :return:
        """
        response = requests.get(
            url=f'{URL}{path}',
            headers=HEADERS,
            params=params
        )
        response.raise_for_status()
        return response

    def get_by_id(self, params, path="/v2/pet/{petId}"):
        """

        :param params:
        :param path:
        :return:
        """
        path = path.format(**params)
        response = requests.get(
            url=f'{URL}{path}',
            headers=HEADERS,
        )
        response.raise_for_status()
        return response
