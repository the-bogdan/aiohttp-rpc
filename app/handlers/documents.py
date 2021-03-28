from datetime import datetime
from database import documents
from sqlalchemy.orm import Session
from rps_request_handler import Validator
from rps_request_handler import RPCHandler


@RPCHandler.register_handler
async def get_document_by_id(params: dict, session: Session):
    """Get document by id from db and returns it as object"""
    Validator.validate('get_document_by_id', params)
    stmt = documents.select().where(documents.c.id == params['id'])
    result = await session.execute(stmt)
    result = result.fetchone()
    return dict(result) if result else result


@RPCHandler.register_handler
async def create_document(params: dict, session: Session):
    """Create document in db and returns it as object"""
    Validator.validate('create_document', params)
    stmt = documents.insert().values(**params).returning(documents)
    result = await session.execute(stmt)
    await session.commit()
    return dict(result.fetchone())


@RPCHandler.register_handler
async def update_document(params: dict, session: Session):
    """Update document by id in db and returns it as object"""
    Validator.validate('update_document', params)
    params['updated_at'] = datetime.now()
    stmt = documents.update() \
        .where(documents.c.id == params['id']) \
        .values(**params) \
        .returning(documents)
    result = await session.execute(stmt)
    result = result.fetchone()
    if result:
        await session.commit()
        return dict(result)
    return None


@RPCHandler.register_handler
async def delete_document(params: dict, session: Session):
    """Delete document by id in db and returns it as object"""
    Validator.validate('delete_document', params)
    stmt = documents.delete() \
        .where(documents.c.id == params['id']) \
        .returning(documents)
    result = await session.execute(stmt)
    result = result.fetchone()
    if result:
        await session.commit()
        return dict(result)
    return None


@RPCHandler.register_handler
async def get_documents(params: dict, session: Session):
    """Get all documents list"""
    Validator.validate('get_documents', params)
    stmt = documents.select().order_by(documents.c.updated_at)
    result = await session.execute(stmt)
    result = [dict(entity) for entity in result.fetchall()]
    return result
