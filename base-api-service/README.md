# base-api-service
- `base-api-service/base_api_service` - package directory
- `base-api-service/tests` - package directory
- `base-api-service/app/controllers` - api routes
- `base-api-service/app/models` - pydantic models
- `base-api-service/app/services` - business services used in the app

### To Get Started:

Enter your credentials in the .env file located in the main directory.

#### if running with docker
Run the app/start the container using: 
    
    docker-compose up --build

To stop the container,
    
    docker-compose down

In your browser, go to http://localhost:8000/docs/ to work with the endpoints with Swagger UI. Otherwise, submit CURL requests through terminal. 

#### if running without docker
Start the Postgres DB
    
    brew services start postgresql

Run the FastAPI backend

    uvicorn app.main:app --reload

In your browser, go to http://localhost:8000/docs/ to work with the endpoints with Swagger UI. Otherwise, submit CURL requests through terminal. 


### Sample CURL request:

    curl -X POST http://localhost:8000/sample-db/ -H 'Content-Type: application/json' -d '{
    "date": "2024-02-28",
    "current_assets": 100000.00,
    "non_current_assets": 500000.00,
    "current_liabilities": 75000.00,
    "non_current_liabilities": 200000.00,
    "shareholders_equity": 325000.00
    }'


    curl -X POST http://127.0.0.1:8000/request-verification/ \
    -H "Content-Type: application/json" \
    -d '{"email": "user@example.com"}'
