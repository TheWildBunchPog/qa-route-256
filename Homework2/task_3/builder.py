from dataclasses import dataclass
import random

import faker

fake = faker.Faker()


@dataclass
class Name:
    category: str
    article: str
    weight_product: dict
    type_product: dict
    color: str
    description: str
    textile_material: dict


class Builder:

    @staticmethod
    def generated_fake_data():
        category = fake.random_choices(['outerwear', 'shirt', 'socks'], 1)[0]

        article = fake.bothify(text=f'OZON_{category}_??##', letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        weight_product = {
            "outerwear": fake.random_int(1000, 10000),
            "shirt": fake.random_int(100, 2000),
            "socks": fake.random_int(10, 300),
        }

        type_product = {
            "outerwear": fake.random_choices(['coat', 'jacket', 'windbreaker'], 1)[0],
            "shirt": fake.random_choices(['casual', 'dress', 'loosefit'], 1)[0],
            "socks": "",
        }

        color = fake.color_name()

        description = fake.text(max_nb_chars=110)

        target = 100
        textile_material = {"cotton": None, "acrylic": None, "viscose": None}
        for i in textile_material:
            number = random.randint(0, target)
            textile_material[i] = number
            target -= number
        textile_material["viscose"] = 100 - (textile_material["cotton"] + textile_material["acrylic"])

        return Name(category, article, weight_product, type_product, color, description, textile_material)
