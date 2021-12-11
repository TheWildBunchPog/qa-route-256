import pytest
from hamcrest import assert_that, equal_to

from super_hero.api.client import ApiClient
from super_hero.checkers.decorators import smoke_check
from super_hero.helpers.base_helpers import get_ids_of_hero_woman, who_stronged
from super_hero.utils.builder import Builder


class TestHeroApiClient:
    client = ApiClient()

    @pytest.mark.parametrize(
        "hero_id",
        [
            pytest.param(Builder().generated_fake_data().hero_id),
            pytest.param(Builder().generated_fake_data().hero_id),
            pytest.param(Builder().generated_fake_data().hero_id),
            pytest.param(Builder().generated_fake_data().hero_id),
            pytest.param(Builder().generated_fake_data().hero_id)
         ]
    )
    @pytest.mark.API
    def test_get_information_of_hero(self, hero_id):
        """Проверка получения информации о герое по id
           Ожидаемый результат: id (генерируем при запросе) == id (получаем в ответ на запрос)"""
        response = self.client.get_information_of_hero(hero_id)
        assert hero_id == int(response.json()["id"])

    @pytest.mark.parametrize(
        "hero_id",
        [
            pytest.param(Builder().generated_fake_data().hero_id),
            pytest.param(Builder().generated_fake_data().hero_id),
            pytest.param(Builder().generated_fake_data().hero_id)
        ]
    )
    @smoke_check
    def test_superhero_example(self, hero_id):
        response = self.client.get_power_stats(hero_id)

        return response

    @pytest.mark.parametrize("woman_hero_id", get_ids_of_hero_woman())
    @pytest.mark.API
    def test_get_information_of_woman_hero(self, woman_hero_id):
        """Проверка, что у всех полученных записей в поле appearance/gender указано Female
           Ожидаемый результат: Female == Female (gender в ответе на запрос в поле appearance/gender)"""
        response = self.client.get_information_of_hero(woman_hero_id)
        gender = response.json()['appearance']['gender']
        assert_that(gender, equal_to('Female'))

    @pytest.mark.API
    def test_battle_of_heroes(self, battle_of_heroes):
        """Сравнение силы персонажей
           Ожидаемый результат: winner (по силе в фикстуре) == winner (по силе в тесте)"""
        hero_one = self.client.get_information_of_hero(battle_of_heroes[0]).json()
        hero_two = self.client.get_information_of_hero(battle_of_heroes[1]).json()

        heroes = [
            {"name": hero_one["name"], "power": int(hero_one["powerstats"]["power"])},
            {"name": hero_two["name"], "power": int(hero_two["powerstats"]["power"])}
        ]

        winner = who_stronged(heroes)

        assert_that(winner, equal_to(battle_of_heroes[2]))
