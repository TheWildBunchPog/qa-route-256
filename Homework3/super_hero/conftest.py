import pytest

from api.client import ApiClient
from helpers.base_helpers import who_stronged
from utils.builder import Builder


@pytest.fixture(scope="function")
def battle_of_heroes() -> list:
    # заполняем словарь heroes двумя героями
    heroes = []
    for _ in range(2):
        while True:
            hero_id = Builder().generated_fake_data().hero_id
            response = ApiClient().get_power_stats(hero_id).json()
            name = ApiClient().get_power_stats(hero_id).json()["name"]
            power = response["power"]
            if power.isdigit():
                break
        heroes.append({"id": hero_id, "name": name, "power": int(power)})
    # сравниваем двух героев по параметрам "power"
    winner = who_stronged(heroes)
    # добавляем результат
    id_heroes_and_winner = [heroes[0]["id"], heroes[1]["id"], winner]

    return id_heroes_and_winner
