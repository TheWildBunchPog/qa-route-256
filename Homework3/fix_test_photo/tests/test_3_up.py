import pytest
import allure

from fix_test_photo.clients.api_client import ApiClient


@allure.title('Test title')
@pytest.mark.parametrize("state, expected", [
    ('pending', 5),
    pytest.param('sold', 10, id='sold test')
])
def test_3_up(state, expected):
    data = {
        "status": state
    }
    return ApiClient().get_find_by_status(params=data).json()
