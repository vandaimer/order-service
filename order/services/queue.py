from datetime import datetime

from aio_pika import connect, Message

from order.config import RABBITMQ_URI, RABBITMQ_USER, RABBITMQ_PASS, \
    RABBITMQ_EXCHANGE, RABBITMQ_ROUTING_KEY


class Queue:
    PRODUCER = 'ORDER_SERVICE'
    TYPE = 'ORDER'

    @staticmethod
    async def get_exchange():
        connection = await connect(
            f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@{RABBITMQ_URI}/',
        )
        channel = await connection.channel()
        exchange = await channel.declare_exchange(RABBITMQ_EXCHANGE,
                                                  auto_delete=True)
        return exchange

    @staticmethod
    async def send_order(order):
        exchange = await Queue.get_exchange()
        message_body = str(Queue.build_message_body(order)).encode()
        message = Message(message_body)

        await exchange.publish(message, routing_key=RABBITMQ_ROUTING_KEY)

    @staticmethod
    def build_message_body(order):
        return {
            'producer': Queue.PRODUCER,
            'type': Queue.TYPE,
            'sent_at': str(datetime.now()),
            'payload': {
                'order': {
                    'order_id': order['id'],
                    'customer_fullname': order['customer_fullname'],
                    'product_name': order['product_name'],
                    'total_amount': order['total_amount'],
                    'created_at': str(order['created_at']),
                }
            }
        }
