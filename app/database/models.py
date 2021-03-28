from sqlalchemy import (
    text,
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
                  Column('created_at', DateTime, server_default=text('now()')),
                  Column('updated_at', DateTime, server_default=text('now()'))
                  )
