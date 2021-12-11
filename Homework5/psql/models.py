from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Animal(Base):
    __tablename__ = 'animals'

    def __repr__(self):
        return f"<Animals(" \
               f"id='{self.id}'," \
               f"species='{self.species}', " \
               f"born_in_captivity='{self.born_in_captivity}', " \
               f"weight='{self.weight}', " \
               f"date_of_birth='{self.date_of_birth}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    species = Column(String(50), nullable=False)
    born_in_captivity = Column(Boolean, nullable=False)
    weight = Column(Float, nullable=False)
    date_of_birth = Column(Date, nullable=False)
