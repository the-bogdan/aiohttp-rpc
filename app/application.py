from aiohttp import web
from rpc_handler import handle_rpc
from database import init_pg_singleton, create_tables


app = web.Application()


app.on_startup.append(create_tables)
app.router.add_route('POST', '/rpc', handle_rpc)
