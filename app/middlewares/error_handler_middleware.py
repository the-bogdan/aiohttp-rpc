from logger import logger
from utils.custom_exceptions import ExecutionException
from aiohttp.web import Request, Response, middleware, json_response


@middleware
async def error_handler_middleware(request: Request, handler) -> Response:
    """Layer handles errors and sends readable response"""
    try:
        return await handler(request)
    except ExecutionException as e:
        return json_response(
            status=e.http_code,
            data={'error': e.error_type, 'message': e.message}
        )
    except BaseException as e:
        logger.error(e, exc_info=True)
        return json_response(
            status=500,
            data={'error': f'{e.__class__.__name__}', 'message': str(e)}
        )
