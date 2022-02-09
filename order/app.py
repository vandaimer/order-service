import time

from fastapi import FastAPI, APIRouter

from order.db import database, create_tables
from order.api import router as order_api
from order.log import logger


application = FastAPI()

router = APIRouter()


@application.on_event("startup")
async def startup():
    await database.connect()
    logger.info('Connected on DB')
    create_tables()


@application.on_event("shutdown")
async def shutdown():
    logger.info('Disconnected from DB')
    await database.disconnect()


@router.get('/{path:path}', status_code=501)
def not_implement(path):
    logger.warning(f'Not implemented path was hit: {path}')
    return {
        'path': f'/{path}',
        'status': 'notImplemented',
        'now': time.time(),
    }


application.include_router(order_api, prefix='/v1')
application.include_router(router)
