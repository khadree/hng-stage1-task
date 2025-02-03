Number Classifier API

A *serverless API* built with *AWS Lambda (Python)* and *API Gateway* that takes a number as input and returns mathematical properties, including whether it is prime, perfect, Armstrong, odd/even, and its digit sum.

Features
- *Deployed on AWS Lambda* via API Gateway
- *Handles CORS* for cross-origin requests
- *Returns JSON responses*
- *Supports GET requests* with a number parameter
- *Fast execution* (<500ms response time)
- *Publicly accessible* endpoint

API Endpoint

https://8vycu7l2i9.execute-api.us-east-1.amazonaws.com/API-Classifier/api/classify-number

Example Request
GET /api/classify-number?number=371

Example Response (200 OK)
json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

Error Response (400 Bad Request)
json
{
    "number": "invalid_input",
    "error": true
}

Setup & Deployment

Prerequisites**
- *AWS Account*
- *AWS CLI installed & configured*
- *Python 3.x*
- *Serverless Framework (Optional)*

Clone Repository**

git clone https://github.com/khadree/hng-stage1-task.git
cd number-classifier-api

Deploy to AWS Lambda**
*Using AWS CLI*
