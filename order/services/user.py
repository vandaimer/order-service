import requests

from order.config import USER_SERVICE_URI
from order.log import logger


class User:
    USER_SERVICE_BASE_URL = f'{USER_SERVICE_URI}/users'

    @staticmethod
    def get_by_id(user_id):
        try:
            response = requests.get(f'{User.USER_SERVICE_BASE_URL}/{user_id}')
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(e)
            raise Exception(f'Error getting user data. User ID: {user_id}')

        return response.json()

    @staticmethod
    def get_fullname(user_id):
        try:
            user = User.get_by_id(user_id)
        except Exception as e:
            logger.warning(e)
            raise e

        firstName = user['firstName']
        lastName = user['lastName']

        return f'{firstName} {lastName}'
