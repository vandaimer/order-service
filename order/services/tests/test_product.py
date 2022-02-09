import json

import pytest

from order.services import Product


class TestProductService:
    def setup_method(self):
        self.mock_product_code = 'mock_product_code'
        self.product_request_url = (f'{Product.PRODUCT_SERVICE_BASE_URL}/'
                                    f'{self.mock_product_code}')
        self.mock_product = {
            'code': self.mock_product_code,
        }

    def test_get_by_code(self, requests_mock):
        requests_mock.get(self.product_request_url,
                          text=json.dumps(self.mock_product))

        response = Product.get_by_code(self.mock_product_code)

        expected = {'code': self.mock_product_code}

        assert response == expected

    def test_get_by_code_raise_exception(self, requests_mock):
        requests_mock.get(self.product_request_url, status_code=500)

        message = (f'Error getting product data. Product Code: '
                   f'{self.mock_product_code}')
        with pytest.raises(Exception, match=message):
            Product.get_by_code(self.mock_product_code)
