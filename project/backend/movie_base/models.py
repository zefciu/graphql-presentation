# coding: utf-8
from sqlalchemy import (
    ARRAY,
    CHAR,
    Column,
    create_engine,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Numeric,
    SmallInteger,
    String,
    Table,
    Text,
    text,
)
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.dialects.postgresql import TSVECTOR
from sqlalchemy.ext.declarative import declarative_base

from movie_base.config import config

engine = create_engine(config['db_connection'], convert_unicode=True)
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
metadata = Base.metadata


class Actor(Base):
    __tablename__ = 'actor'

    actor_id = Column(Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False, index=True)
    last_update = Column(DateTime, nullable=False,
                         server_default=text("now()"))


class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    last_update = Column(DateTime, nullable=False,
                         server_default=text("now()"))


class Language(Base):
    __tablename__ = 'language'

    language_id = Column(Integer, primary_key=True)
    name = Column(CHAR(20), nullable=False)
    last_update = Column(DateTime, nullable=False,
                         server_default=text("now()"))


class Film(Base):
    __tablename__ = 'film'

    film_id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=False)
    release_year = Column(Integer)
    language_id = Column(
        ForeignKey(
            'language.language_id',
            ondelete='RESTRICT',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    original_language_id = Column(
        ForeignKey(
            'language.language_id',
            ondelete='RESTRICT',
            onupdate='CASCADE'),
        index=True)
    rental_duration = Column(
        SmallInteger, nullable=False, server_default=text("3"))
    rental_rate = Column(Numeric(4, 2), nullable=False,
                         server_default=text("4.99"))
    length = Column(SmallInteger)
    replacement_cost = Column(
        Numeric(5, 2), nullable=False, server_default=text("19.99"))
    rating = Column(
        Enum(
            'G',
            'PG',
            'PG-13',
            'R',
            'NC-17',
            name='mpaa_rating'),
        server_default=text("'G'::mpaa_rating"))
    last_update = Column(DateTime, nullable=False,
                         server_default=text("now()"))
    special_features = Column(ARRAY(Text()))
    fulltext = Column(TSVECTOR, nullable=False, index=True)

    language = relationship(
        'Language',
        primaryjoin='Film.language_id == Language.language_id'
    )
    original_language = relationship(
        'Language',
        primaryjoin='Film.original_language_id == Language.language_id'
    )
    actors = relationship(
        'Actor',
        secondary=lambda: film_actor_table, backref='films'
    )


film_actor_table = Table(
    'film_actor',
    Base.metadata,
    Column('actor_id', Integer, ForeignKey(
        'actor.actor_id', ondelete='RESTRICT', onupdate='CASCADE'
    ), primary_key=True, nullable=False),
    Column('film_id', Integer, ForeignKey(
        'film.film_id', ondelete='RESTRICT', onupdate='CASCADE'
    ), primary_key=True, nullable=False)
)


class FilmCategory(Base):
    __tablename__ = 'film_category'

    film_id = Column(
        ForeignKey(
            'film.film_id',
            ondelete='RESTRICT',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False)
    category_id = Column(
        ForeignKey(
            'category.category_id',
            ondelete='RESTRICT',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False)
    last_update = Column(DateTime, nullable=False,
                         server_default=text("now()"))

    category = relationship('Category')
    film = relationship('Film')
