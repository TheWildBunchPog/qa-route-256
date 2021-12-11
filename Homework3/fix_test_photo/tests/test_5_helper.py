import pytest
import allure

from fix_test_photo.clients.api_client import ApiClient
from fix_test_photo.helpers.base_helper import get_filtered_animal_name


@allure.title('Test title')
@pytest.mark.parametrize("state, expected", [
    pytest.param('sold', 10, id='sold test'),
    pytest.param('available', 580, id='available test'),
])
def test_5_helper(state, expected):
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
    animal_with_filter = get_filtered_animal_name(pet_list=pet_list)

    print(animal_with_filter)
    return animal_with_filter
