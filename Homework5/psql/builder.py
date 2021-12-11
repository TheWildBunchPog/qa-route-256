from psql.models import Animal


class PostgreSQLBuilder:

    def __init__(self, client):
        self.client = client

    def create_animal(self, species=None, born_in_captivity=None, weight=None, date_of_birth=None):
        animal = Animal(
            species=species,
            born_in_captivity=born_in_captivity,
            weight=weight,
            date_of_birth=date_of_birth
        )
        self.client.session.add(animal)
        self.client.session.commit()  # no need if sessionmaker autocommit=True
        return animal

    def get_animal(self, animal_id):
        res = self.client.session.query(Animal).filter_by(id=animal_id).all()[0]
        self.client.session.expire_all()
        return {'species': res.species, 'born_in_captivity': res.born_in_captivity, 'weight': res.weight, 'date_of_birth': res.date_of_birth}

    def delete_animal(self, animal_id):
        res = self.client.session.query(Animal).filter_by(id=animal_id)
        res.delete()
        self.client.session.commit()

    def delete_all_animal(self):
        res = self.client.session.query(Animal)
        res.delete()
        self.client.session.commit()
