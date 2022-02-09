import json

import pytest

from order.services import User


class TestUserService:
    def setup_method(self):
        self.mock_user_id = 'mock_user_id'
        self.mock_user = {
            'id': self.mock_user_id,
        }
        self.user_request_url = (f'{User.USER_SERVICE_BASE_URL}/'
                                 f'{self.mock_user_id}')

    def test_get_by_id(self, requests_mock):
        requests_mock.get(self.user_request_url,
                          text=json.dumps(self.mock_user))

        expected = {'id': self.mock_user_id}

        response = User.get_by_id(self.mock_user_id)

        assert response == expected

    def test_get_by_id_raise_exception(self, requests_mock):
        requests_mock.get(self.user_request_url, status_code=500)

        message = f'Error getting user data. User ID: {self.mock_user_id}'
        with pytest.raises(Exception, match=message):
            User.get_by_id(self.mock_user_id)

    def test_get_fullname(self, mocker):
        mock_user = {
            **self.mock_user,
            'lastName': 'lastName',
            'firstName': 'firstName'
        }
        mocker.patch(
            'order.services.User.get_by_id',
            side_effect=lambda x: mock_user)

        user_fullname = User.get_fullname(self.mock_user_id)
        expected = 'firstName lastName'

        assert user_fullname == expected
