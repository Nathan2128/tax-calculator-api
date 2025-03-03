# Tax Calculator API

This is a Flask-based HTTP API built as a take-home interview assignment. 
The API calculates the total income tax, tax breakdown per bracket, and the effective tax rate for a given annual salary and tax year. It uses Flask, flask-smorest, and marshmallow for request handling, input validation, and OpenAPI (Swagger) documentation generation.

## Features

* Marginal Tax Calculation:
Calculates total tax using marginal tax rates based on provided tax brackets.

* Tax Breakdown:
Returns a breakdown of the tax computed for each bracket.

* Effective Rate Calculation:
Computes the effective tax rate (total tax divided by salary).

* External API Integration:
Fetches tax brackets from an external, dockerized API endpoint (e.g., /tax-calculator/tax-year/2021).

* Retry Logic:
Automatically retries external API calls (up to 2 retries for HTTP 500 responses) using a custom retry-enabled session.

* Swagger UI Documentation:
Generates interactive API documentation using flask-smorest and Swagger UI.

## Running the project:

1. ```git clone https://github.com/<your-username>/tax-calculator-api.git```
2.  ```cd tax-calculator-api```
3.  ```python3 -m venv venv```
4.  ```source venv/bin/activate```
5.  ```pip install -r requirements.txt```
6.  Make sure external dependency docker is running at http://localhost:5001/tax-calculator/tax-year/<year>
7. To start the flask server run ```flask run```

Hit this URL for API docs: ```http://localhost:5000/swagger-ui```


![image](https://github.com/user-attachments/assets/114479ff-6c66-4199-b1d7-8966a2a2a0c1)



