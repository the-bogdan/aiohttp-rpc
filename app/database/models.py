from sqlalchemy import (
    Table,
    Column,
    String,
    Integer,
    MetaData,
    DateTime
)


metadata = MetaData()


documents = Table('documents', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String),
                  Column('created_at', DateTime),
                  Column('updated_at', DateTime)
)

