from config import config
from asyncpgsa import pg
from database.models import metadata
from sqlalchemy.dialects.postgresql.base import PGDialect
from sqlalchemy.sql.ddl import CreateTable, DropTable


async def init_pg_singleton(app=None):
    await pg.init(**config['postgresql'])


async def update_tables():
    await init_pg_singleton()
    async with pg.begin() as conn:
        for table in metadata.sorted_tables:
            query = DropTable(table, if_exists=True)
            query_str = str(query.compile(dialect=PGDialect()))
            await conn.execute(query_str)
            query = DropTable(table, if_exists=True)
            query_str = str(query.compile(dialect=PGDialect()))
            await conn.execute(query_str)


async def create_tables(app=None):
    await init_pg_singleton()
    async with pg.begin() as conn:
        for table in metadata.sorted_tables:
            query = CreateTable(table, if_not_exists=True)
            query = str(query.compile(dialect=PGDialect()))
            await conn.execute(query)
