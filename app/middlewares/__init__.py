from .error_handler_middleware import error_handler_middleware
from .response_middleware import response_middleware
from .session_middleware import session_middleware

# order is important!
middlewares_list = [
    error_handler_middleware,
    session_middleware,
    response_middleware
]
