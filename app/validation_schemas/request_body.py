from validator import Validator
from rps_request_handler import RPCHandler

Validator.schema('request_body', {
    'type': 'object',
    'properties': {
        'action': {'type': 'string', 'enum': list(getattr(RPCHandler, '_handlers').keys())},
        'params': {'type': 'object'}
    },
    'required': ['action', 'params'],
    'additionalProperties': False
})
