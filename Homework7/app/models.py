from sqlalchemy import Column, Integer, String
from database import Base


class Wall(Base):
    __tablename__ = 'message_wall'
    id = Column(Integer, primary_key=True)
    author = Column(String(100))
    comment = Column(String(100))

    def __init__(self, author=None, comment=None):
        self.author = author
        self.comment = comment

    def __repr__(self):
        return f"<Test(" \
               f"id='{self.id}'," \
               f"author='{self.author}', " \
               f"comment='{self.comment}', " \
               f")>"
