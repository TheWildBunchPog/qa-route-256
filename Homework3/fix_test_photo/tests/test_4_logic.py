import pytest
import allure

from fix_test_photo.clients.api_client import ApiClient


@allure.title('Test title')
@pytest.mark.parametrize("state, expected", [
    pytest.param('sold', 10, id='sold test'),
    pytest.param('available', 580, id='available test'),
])
def test_4_logic(state, expected):
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

    # get all name for animal in category
    count = list()
    for pet in pet_list:
        category = pet.get('category', None)
        if category and 'string' not in category.get('name'):
            count.append(category.get('name'))
    print(count)
    return count
