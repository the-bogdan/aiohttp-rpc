from validator import Validator


Validator.schema('get_document_by_id', {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'}
    },
    'required': ['id'],
    'additionalProperties': False
})

Validator.schema('create_document', {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'}
    },
    'required': ['name'],
    'additionalProperties': False
})

Validator.schema('update_document', {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'name': {'type': 'string'}
    },
    'required': ['id'],
    'additionalProperties': False
})

Validator.schema('delete_document', {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'}
    },
    'required': ['id'],
    'additionalProperties': False
})

Validator.schema('get_documents', {
    'type': 'object',
})
