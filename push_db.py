from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from flask import Flask, render_template

#Настройка бд
engine = create_engine('sqlite:///blog.db')
Base = declarative_base()

class Post(Base):
  __tablename__ = 'posts'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  content = Column(Text)

# Создание базы данных и таблицы
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
for i in range(1, 5):
    my_first_post = Post(title = 'My post', content = 'Hello, my first post in my block')
    session.add(my_first_post)
    session.commit()