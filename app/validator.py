from jsonschema import validate
from jsonschema.exceptions import ValidationError
from utils.custom_exceptions import ExecutionException


class Validator:
    _schemas = dict()

    @classmethod
    def schema(cls, action: str, schema: dict):
        """Add new schema. The action must be equal to handler function name"""
        if action in cls._schemas:
            raise KeyError(f'JSON schema for action {action} already exists')
        cls._schemas[action] = schema

    @classmethod
    def validate(cls, action, body):
        """Validate data by action"""
        schema = cls._schemas.get(action)
        if not schema:
            raise KeyError(f'JSON schema for action {action} does not exists')
        try:
            validate(body, schema)
        except ValidationError as e:
            raise ExecutionException('json-schema-error', e.message, 415)
