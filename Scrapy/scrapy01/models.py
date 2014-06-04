from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declatative import declatative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase=declarative_base()

def db_connect():
    return create_engine(URL(**settings.DATABASE))

def create_scrapy01_tabel(engine):
    DeclarativeBase.metadata.create_all(engine)

class Scripy01(DeclarativeBase):
    __tablename__=='scripy01'
    id=Column(Integer,primary_key=True)
    title=Column('title',String(200))
    link=Column('link',String(200))
