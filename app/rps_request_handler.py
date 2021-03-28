from typing import Callable
from validator import Validator
from json.decoder import JSONDecodeError
from aiohttp.web import Request, Response
from utils.custom_exceptions import ExecutionException


class RPCHandler:
    """
    Base class accumulate all rpc actions which are decorated by
    register_handler method and provide method for handle rpc request
    and make response
    """
    _handlers = dict()

    @classmethod
    async def handle_rpc(cls, request: Request) -> Response:
        """Method handle rpc action and params and call function for handling it"""
        body = await cls._get_body(request)
        Validator.validate('request_body', body)
        return await cls._handlers.get(body['action'])(body['params'], request['db_session'])

    @classmethod
    def register_handler(cls, func: Callable):
        """Decorator which register function or method as rpc action handler"""
        cls._handlers[func.__name__] = func
        return func

    @staticmethod
    async def _get_body(request: Request) -> dict:
        """Checks content type and returns json body as a dict"""
        if request.content_type != 'application/json':
            message = 'Only application/json content-type supported'
            raise ExecutionException('content-type-error', message, 415)
        try:
            return await request.json()
        except JSONDecodeError:
            message = 'Body is not a valid json object. Cannot decode it'
            raise ExecutionException('json-decode-error', message, 415)

