from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from main import db

class Category(db.Model):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=True, unique=True)
    words = relationship("Word", backref='category')

    def __repr__(self):
        return '<Category %r>' % self.name

class Word(db.Model):
    __tablename__ = 'word'

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=True)
    spelling = Column(String(20), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return '<Word %r>' % self.spelling

def db_init():
    db.create_all()