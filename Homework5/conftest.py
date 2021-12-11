import pytest

from psql.client import PostgreSQLClient


@pytest.fixture(scope='session')
def psql_client():
    psql_client = PostgreSQLClient(user='test', password='test', db_name='test')
    psql_client.connect()
    yield psql_client
    psql_client.connection.close()


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        psql_client = PostgreSQLClient(user='test', password='test', db_name='test')

        psql_client.connect()
        psql_client.create_animals()
        psql_client.connection.close()
