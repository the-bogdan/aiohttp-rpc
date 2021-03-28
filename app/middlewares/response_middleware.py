from typing import Any
from datetime import datetime, date
from utils.custom_exceptions import ExecutionException
from aiohttp.web import Response, Request, middleware, json_response


@middleware
async def response_middleware(request: Request, handler) -> Response:
    """Layer opens database connection during handling request"""
    response = await handler(request)
    if isinstance(response, Response):
        return response
    if isinstance(response, (dict, list)):
        return json_response(serialize_object(response))
    raise ExecutionException('entity-error', 'Не удалось найти или создать сущность')


def serialize_object(obj: Any) -> Any:
    """Method goes recursively through all items in list or dict and make its JSON Serializable"""
    if isinstance(obj, str):
        return obj
    if isinstance(obj, int):
        return obj
    if isinstance(obj, dict):
        result = dict()
        for key, value in obj.items():
            result[key] = serialize_object(value)
        return result
    if isinstance(obj, list):
        result = list()
        for item in obj:
            result.append(serialize_object(item))
        return result
    if isinstance(obj, datetime):
        return str(obj.strftime('%Y-%m-%d %H:%M:%S'))
    if isinstance(obj, date):
        return str(date)
    return str(obj)
