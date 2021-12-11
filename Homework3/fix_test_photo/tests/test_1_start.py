import requests


def test_1_simple():
    # Act
    """curl -X 'GET' \
  'https://petstore.swagger.io/v2/pet/findByStatus?status=pending' \
  -H 'accept: application/json'"""
    URL = "https://petstore.swagger.io"
    ENDPOINT = "/v2/pet/findByStatus"
    CONDITION = "status=pending"
    swagger_url = f'{URL}{ENDPOINT}?{CONDITION}'

    # Arrange
    response = requests.get(url=swagger_url)
    response.raise_for_status()
    print(swagger_url, response.status_code)

    # Assert
    assert response.status_code == requests.codes.all_good
