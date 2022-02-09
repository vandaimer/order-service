import requests

from order.config import PRODUCT_SERVICE_URI
from order.log import logger


class Product:
    PRODUCT_SERVICE_BASE_URL = f'{PRODUCT_SERVICE_URI}/products'

    @staticmethod
    def get_by_code(product_code):
        try:
            url = f'{Product.PRODUCT_SERVICE_BASE_URL}/{product_code}'
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            message = (f'Error getting product data.'
                       f' Product Code: {product_code}')
            logger.error(e)
            raise Exception(message)

        return response.json()
