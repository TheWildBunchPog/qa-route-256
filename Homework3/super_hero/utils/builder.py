from dataclasses import dataclass
import faker


fake = faker.Faker()


@dataclass
class Name:
    hero_id: int


class Builder:

    @staticmethod
    def generated_fake_data():
        hero_id = fake.randomize_nb_elements(number=700, le=True, min=1)

        return Name(hero_id)
