import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email= Column(String(250), nullable=False, unique=True)
    password =Column(String(250), nullable=False)
    follower = relationship ('Follower')

class Follower (Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_code = Column(String(250), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship (User)

class Post(Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,  ForeignKey('user.id'), nullable=False)
    content = Column(String(250), nullable=False)
    user= relationship(User)  

class Comment(Base):
    __tablename__= 'comment'
    id = Column(Integer, primary_key=True)
    post_id =Column(Integer, ForeignKey('post.id'), nullable=False)
    autor_id= Column(Integer, ForeignKey('user.id'), nullable=False)  
    text_comment=Column(String(250), nullable=False) 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
