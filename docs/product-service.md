## Product Service

### Endpoint

| HTTP Method |           Path           | Description                  |
|-------------|:------------------------:|------------------------------|
| GET         | /products/{product_code} | Retrieves a specific product |


### Mocked Values

| Product Code | Status Code | Delay |
|--------------|:-----------:|:-----:|
| classic-box  |     200     | 200ms |
| family-box   |     200     |  60s  |
| veggie-box   |     500     | 200ms |


**NOTE**: Status code and delay are hardcoded per product code to simulate faults.
