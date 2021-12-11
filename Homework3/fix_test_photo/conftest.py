import pytest
from random import choice

from fix_test_photo.clients.api_client import ApiClient
from fix_test_photo.helpers.base_helper import get_animal_with_photo


@pytest.fixture
def id_for_available_with_photo():
    data = {
        "status": 'available'
    }
    pet_list = ApiClient().get_find_by_status(params=data).json()
    animal_with_info = get_animal_with_photo(pet_list)
    return choice(list(animal_with_info.keys()))
