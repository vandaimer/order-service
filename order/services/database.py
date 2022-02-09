from order.db import database
from order.log import logger


class Database:
    @staticmethod
    async def insert(model, values):
        query = model.insert().values(**values)
        record = await database.execute(query)
        logger.info(f'New {str(model)} inserted with {str(values)}')

        return record
