import pytest
import allure
from random import choice

from fix_test_photo.clients.api_client import ApiClient
from fix_test_photo.helpers.base_helper import get_animal_with_photo


@allure.title('Test title')
@pytest.mark.parametrize("state, expected", [
    pytest.param('sold', 10, id='sold test'),
    pytest.param('available', 580, id='available test'),
])
def test_6_photo(state, expected):
    """
    {'id': 1122338462572, 'category': {'id': 5436, 'name': 'soaspec_test'},
    'name': 'Charlie', 'photoUrls': ['string'],
    'tags': [{'id': 1, 'name': 'string'}],
    'status': 'sold'}
    :param state:
    :param expected:
    :return:
    """
    data = {
        "status": state
    }
    pet_list = ApiClient().get_find_by_status(params=data).json()
    animal_with_photo = get_animal_with_photo(pet_list)

    random_animal_id = choice(list(animal_with_photo.keys()))

    data = {
        "petId": random_animal_id
    }
    animal_info = ApiClient().get_by_id(params=data).json()
    print(animal_info)
    return animal_info
