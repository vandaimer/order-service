from datetime import datetime
from unittest.mock import AsyncMock

import pytest
from freezegun import freeze_time

from order.models import Orders
from order.schemas import OrderInSchema
from order.views import Order

pytestmark = pytest.mark.asyncio


class TestOrderView:
    def setup_method(self):
        self.mock_user_id = 'user_id'
        self.mock_product_code = 'product_code'
        self.mock_user_fullname = 'user_fullname'
        self.mock_product_name = 'product_name'

        self.mock_order_input = {
            'user_id': self.mock_user_id,
            'product_code': self.mock_product_code,
        }

        self.mock_product = {
            'product_code': self.mock_product_code,
            'name': self.mock_product_name,
            'price': 1,
        }

        self.new_order_id = 123

    @freeze_time('2021-04-25')
    async def test_create(self, mocker):
        spy_queue = mocker.patch('order.services.Queue.send_order')
        spy_user = mocker.patch('order.services.User.get_fullname',
                                return_value=self.mock_user_fullname)
        spy_product = mocker.patch('order.services.Product.get_by_code',
                                   return_value=self.mock_product)
        spy_database = mocker.patch('order.services.Database.insert',
                                    side_effect=AsyncMock(
                                        return_value=self.new_order_id
                                    ))

        order_input = OrderInSchema(**self.mock_order_input)

        expected_input = {
            'customer_fullname': self.mock_user_fullname,
            'product_name': self.mock_product_name,
            'product_code': self.mock_product_code,
            'user_id': 'user_id',
            'total_amount': 1,
            'created_at': datetime.now(),
        }

        expected_result = {
            **expected_input,
            'id': self.new_order_id,
        }

        result = await Order.create(order_input)

        spy_user.assert_called_once_with(self.mock_user_id)
        spy_product.assert_called_once_with(self.mock_product_code)
        spy_database.assert_called_once_with(Orders, expected_input)
        spy_queue.assert_called_once()

        assert result == expected_result
