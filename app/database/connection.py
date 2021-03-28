from config import config
from database.models import metadata
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


engine = create_async_engine(URL(**config['postgresql']))
context_session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    class_=AsyncSession
)


async def update_tables(*args, **kwargs):
    """Drop existing tables in database and create new"""
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)


async def create_tables(*args, **kwargs):
    """Create tables thad doesn't exists already"""
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
