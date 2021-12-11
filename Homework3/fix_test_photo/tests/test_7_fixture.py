import allure
import pytest
from hamcrest import assert_that, contains_string

from fix_test_photo.clients.api_client import ApiClient


@allure.title('Test title')
@pytest.mark.parametrize('iterate', range(10))
def test_7_fixture(iterate, id_for_available_with_photo):
    data = {
        'petId': id_for_available_with_photo
    }
    animal_info = ApiClient().get_by_id(params=data).json()
    print(animal_info)

    # assert_that(animal_info, is_in(any('http')
    for line in animal_info.get('photoUrls', list()):
        assert_that(actual=line,
                    matcher=contains_string('http'),
                    reason=f'No found link in {animal_info.get("photoUrls")}')
    return animal_info
