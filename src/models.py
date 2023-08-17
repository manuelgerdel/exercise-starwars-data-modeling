import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# No editar nada de aquí para arriba


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.

    # Generics
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    email = Column(String(100), nullable=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    password = Column(String(30), nullable=False)
    subscription_date = Column(String(8), nullable=False)
    # Relations
    favorite = relationship("Favorites", back_populates="user")


class Favorites(Base):
    __tablename__ = 'favorites'

    #Generics
    id = Column(Integer, primary_key=True)
    favorite_type = Column(String(20), nullable=False)
    #Relations
    planets_id = Column(Integer, ForeignKey("planets.id"), nullable=True)
    characters_id = Column(Integer, ForeignKey("characters.id"), nullable=True)
    vehicles_id = Column(Integer, ForeignKey("vehicles.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False) 
    

class Planets(Base):
    __tablename__ = 'planets'

    #Generics
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    population = Column(Integer, nullable=False)
    #Relations
    favorites = relationship("Favorites", back_populates = "planets")

class Characters(Base):
    __tablename__ = 'characters'

    #Generics
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    gender = Column(String(20), nullable=False)
    #Relations
    favorites = relationship("Favorites", back_populates = "characters")

class Vehicles(Base):
    __tablename__ = 'vehicles'

    #Generics
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    model = Column(String(20), nullable=False)
    #Relations
    favorites = relationship("Favorites", back_populates = "vehicles")



# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
