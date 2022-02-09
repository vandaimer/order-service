# Implement Order microservice
---

## Technologies
- Framework [FastAPI](fastAPi.tiangolo.com)
- ORM - [SQLAlchemy](https://www.sqlalchemy.org/)/[databases](https://pypi.org/project/databases/)
- PostgreSQL as database system (SGBD)

## Design process
 1. Read all files/informations on the repository
 2. Collect all requirements (Framework, ORM, SGBD, external microservices usage...)
 3. Run the docker-compose services and test User and Product service in order to understand how they work
 4. Knowing the requirements, I made a brief picture in my mind on how the things would work/organized
    * module to access external services
    * module to have models
    * module to have schemas
    * and so on...
 5. Implemented the first endpoint (POST) returning a mocked data
 6. Implemented a view (Order) that has the business logic, but returning mocked data and connected on the endpoint.
 7. Implemented a service (User service), made it return a mocked data and connected on the Order view (later I did the same for Product service)
 8. Here tested the endpoint in the whole chain, *ENDPOINT -> VIEW -> USER|PRODUCT* service, and still returning mocked data
 9. Implemented the second version of User service taking data from the user-service via HTTP. Also, implemented the unit tests - The same for Product service
 10. Tested the whole chain using real data from the external services
 11. Since last step, I needed to handle the HTTP exceptions - Including on the [route](https://github.com/vandaimer/order-service/blob/main/order/api.py#L16)
 12. Installed flake8 to fix pep8 issues before write more code
 13. Connected with Database and stored orders there
 14. Moment later I created a service called Database to abstract db operations and help me on the unit test side. **P.S.: This code should be move to db.py**
 15. Having the business logic working fine (without sending the data to RabbitMQ), I implemented unit tests for the Order view
 16. Since from the start, I did stuffs that I judged as something faster to be done first, so decided to add logs
 17. Implemented Queue service to send the order data to RabbitMQ
 18. Tested the whole process and saw messages coming into RabbitMQ by Dashboard
 29. Reviewed the unit tests of views.Order.py
 20. All testes above, I was using a user that has a "timeout", so works once, fails the next and so on. From here, I understood the difference between the user/product delay/error behavior
 21. Added Newrelic agent and added on the log module. There we can see:
     * How many requests was recived
     * How many requests failed
     * Which endpoints have been used
     * And so on...
 22. Made more tests to try to find any issues - All the time has "bug ghost".
 23. Reviewd the setup of the project - docker-compose etc

## Project Organization
* services/ - Responsible for access external services such as user-service, product-service and RabbitMQ.
* views/ - Responsible for handle business logic only.
* api.py - Has the API endpoint definition only. For this project, only one file is enough. For larger projects, we can create a package and splint in more files.
* app.py - Start the frameowork (FastAPI), connect/disconnect into database and set the endpoints availables
* config.py - Responsible for take data from the environment vars, or define a generic config
* db.py - Responsible for handling the DB connection and ORM (SQLAlchemy/databases) stuff
* log.py - Responsible for creating a logger for the whole application. On larger applications, we can configure many loggers for different purposes
* models.py - Has the db tables definitions
* schemas.py - Has the schemas used by the framework. We can define the contract of input and output of each endpoint.

# How to use it
### How to run the API
 - Start the database first, sometimes it starts delay a bit: `docker-compose up -d database`
 - Start the order-service: `docker-compose up order-service`

### Endpoints

The endpoint is: `POST http://localhost:8000/v1/order`

Body example:

```
{
	"user_id": "7c11e1ce2741",
	"product_code": "classic-box"
}
```

cURL example:

```
curl -XPOST http://localhost:8000/v1/order \
  -H 'Content-Type: application/json' \
  -d '{
	"user_id": "7c11e1ce2741",
	"product_code": "classic-box"
}'
```

Also, you're able to use the documentations of it accessing:

- http://localhost:8000/docs
- http://localhost:8000/redoc

### How to run the unit tests
 - Run: `docker-compose up tests`


## Improvements


- Add migrations (SQLAlchemy Migrations)
- Improve the logs that are sending to Newrelic
- Implement an endpot of healthcheck - Is should at least test the connection beetween database (PostgreSQL) and Queue (RabbitMQ)
- Improve the way the code handle error that may have on RabbitMQ - Today the code is just logging the possible error. A better implementation should have a flag on Order model callend (published=TRUE|FALSE), default is FALSE, if the Order was sent successfully, this flag is changed to TRUE, if not, remains FALSE, and we can identify the Orders that was not sent to the queue.
- Add a fixed timeout on requests to user/product service. It's known that some user/product requests have up to 60 seconds of delay.

## 3rd-Party services


Here is the credentials of the Newrelic account. Don't worry, it's an account only for this project. There you'll see some logs/metrics. 

P.S.: I did't spend much time configurint it.

User: giroca9931@laraskey.com
Pass: 32FZB3fj9SF5UQ8tzzdc
