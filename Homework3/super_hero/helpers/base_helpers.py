import re

from super_hero.api.client import ApiClient


def get_ids_of_hero_woman() -> dict:
    # парсим страницу с героями
    html_page = ApiClient().get_ids_of_heroes().text
    heroes = html_page[html_page.find('Chracter Name'):(html_page.find('701'))]
    result = re.findall('<.*\w>(\w.*)</.*>', heroes)

    # вытаскиваем имена персонажей, с "woman" в имени
    id_and_woman_hero = {}
    for i in range(0, len(result), 2):
        if 'woman' in result[i + 1].lower():
            id_and_woman_hero.update({int(result[i]): result[i + 1]})

    return id_and_woman_hero


def who_stronged(heroes) -> str:
    if heroes[0]["power"] > heroes[1]["power"]:
        who_winner = heroes[0]["name"]
    elif heroes[0]["power"] < heroes[1]["power"]:
        who_winner = heroes[1]["name"]
    else:
        who_winner = "Силы равны"
    return who_winner
