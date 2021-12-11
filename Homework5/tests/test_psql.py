import pytest

from psql.builder import PostgreSQLBuilder


class PostgreSQLBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, psql_client):
        self.psql = psql_client
        self.psql_builder = PostgreSQLBuilder(psql_client)


class TestPsql(PostgreSQLBase):

    def test_add_animals(self):
        # добавляем 5 разных животных в таблицу
        panda = self.psql_builder.create_animal(species='Panda', born_in_captivity=True, weight='80.5', date_of_birth='2010-05-25')
        lion = self.psql_builder.create_animal(species='Lion', born_in_captivity=False, weight='191.7', date_of_birth='2012-02-05')
        dolphin = self.psql_builder.create_animal(species='Dolphin', born_in_captivity=True, weight='200.2', date_of_birth='1990-01-23')
        penguin = self.psql_builder.create_animal(species='Penguin', born_in_captivity=False, weight='36.6', date_of_birth='2008-08-06')
        giraffe = self.psql_builder.create_animal(species='Giraffe', born_in_captivity=True, weight='700.1', date_of_birth='2002-07-17')

        # получаем одну запись из таблицы
        get_dolphin = self.psql_builder.get_animal(dolphin.id)

        # проверяем, что животное, которое мы получили, соответствует записанному
        assert len(get_dolphin["species"]) > 0
        assert isinstance(get_dolphin['born_in_captivity'], bool)
        assert get_dolphin['weight'] > 0
        assert dolphin.date_of_birth == get_dolphin["date_of_birth"]

        # удаляем ранее добавленные записи из таблицы
        self.psql_builder.delete_animal(panda.id)
        self.psql_builder.delete_animal(lion.id)
        self.psql_builder.delete_animal(dolphin.id)
        self.psql_builder.delete_animal(penguin.id)
        self.psql_builder.delete_animal(giraffe.id)
