from sqlalchemy import MetaData, create_engine
from databases import Database

from order.config import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, \
    DATABASE_NAME


database_uri = (f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}'
                f'@{DATABASE_HOST}/{DATABASE_NAME}')

engine = create_engine(database_uri)

metadata = MetaData()

database = Database(database_uri)


def create_tables():
    metadata.create_all(engine)
