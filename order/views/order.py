from datetime import datetime

from order.models import Orders
from order.services import User, Product, Queue, Database
from order.log import logger


class Order:

    @staticmethod
    async def create(order):
        user_fullname = User.get_fullname(order.user_id)
        product = Product.get_by_code(order.product_code)

        new_order = {
            **order.dict(),
            'customer_fullname': user_fullname,
            'product_name': product['name'],
            'total_amount': product['price'],
            'created_at': datetime.now(),
        }

        new_order_id = await Database.insert(Orders, new_order)

        new_order = {
            'id': new_order_id,
            **new_order,
        }

        try:
            await Queue.send_order(new_order)
        except Exception as e:
            # Having time I'll implement a flag (published=TRUE|FALSE)
            # on models.Orders to identify
            # Orders that didn't get send to the Quque
            logger.error(e)

        return new_order
