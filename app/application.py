# its need for register handler and schemas and dont get circle import error
import handlers
import validation_schemas

from aiohttp import web
from database import create_tables
from middlewares import middlewares_list
from rps_request_handler import RPCHandler


app = web.Application(middlewares=middlewares_list)

app.on_startup.append(create_tables)
app.router.add_route('POST', '/rpc', RPCHandler.handle_rpc)
