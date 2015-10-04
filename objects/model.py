from peewee import Model, CharField, PostgresqlDatabase, DateField
from playhouse.shortcuts import model_to_dict
from config import DBNAME, DBUSER

from utilities.json import parseObjectToJson

__author__ = 'Blackleg'

psql_db = PostgresqlDatabase(DBNAME, user=DBUSER)

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = psql_db


class QuoteOfDay(BaseModel):
    quote = CharField()
    author = CharField()
    date = DateField()

def removeIdProperty(dict):
    del dict['id']

def parseModelToJson(model):
    dict = model_to_dict(model)
    removeIdProperty(dict)
    return parseObjectToJson(dict)


def connectModel():
    psql_db.connect()

def closeModel():
    if not psql_db.is_closed():
        psql_db.close()

def initModel():
    connectModel()
    if not QuoteOfDay.table_exists():
        QuoteOfDay.create_table()
        QuoteOfDay.create(quote='The Quote Of the Day', author='Blackleg', date='2001-10-05')
    closeModel()



