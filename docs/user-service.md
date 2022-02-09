## User Service

### Endpoint

| HTTP Method |       Path       | Description               |
|-------------|:----------------:|---------------------------|
| GET         | /users/{user_id} | Retrieves a specific user |

### Mocked Values

| User ID      |      Status Code       | Delay |
|--------------|:----------------------:|:-----:|
| 7c11e1ce2741 |          200           | 300ms |
| e6f24d7d1c7e | Alternates 200 and 500 | 300ms |


**NOTE**: Status code and delay are hardcoded per user id to simulate faults.
