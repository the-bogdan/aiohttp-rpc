from jsonschema import validate
from jsonschema.exceptions import ValidationError
from utils.custom_exceptions import ExecutionException


class Validator:
    _schemas = dict()

    @classmethod
    def schema(cls, method: str, schema: dict):
        """Add new schema. The method must be equal to handler function name"""
        if method in cls._schemas:
            raise KeyError(f'JSON schema for method {method} already exists')
        cls._schemas[method] = schema

    @classmethod
    def validate(cls, method, body):
        """Validate data by method"""
        schema = cls._schemas.get(method)
        if not schema:
            raise KeyError(f'JSON schema for method {method} does not exists')
        try:
            validate(body, schema)
        except ValidationError as e:
            raise ExecutionException('json-schema-error', e.message, 415)
