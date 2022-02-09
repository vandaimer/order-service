from datetime import datetime

from freezegun import freeze_time

from order.services import Queue


class TestQueueService:
    def setup_method(self):
        self.mock_order = {
            'id': 'id',
            'customer_fullname': 'customer_fullname',
            'product_name': 'product_name',
            'total_amount': 'total_amount',
            'created_at': 'created_at',
        }

    @freeze_time('2021-04-21')
    def test_build_messsage_body(self, mocker):
        expected = {
            'producer': Queue.PRODUCER,
            'type': Queue.TYPE,
            'sent_at': str(datetime.now()),
            'payload': {
                'order': {
                    'order_id': self.mock_order['id'],
                    'customer_fullname': self.mock_order['customer_fullname'],
                    'product_name': self.mock_order['product_name'],
                    'total_amount': self.mock_order['total_amount'],
                    'created_at': str(self.mock_order['created_at']),
                }
            }
        }
        result = Queue.build_message_body(self.mock_order)

        assert result == expected
