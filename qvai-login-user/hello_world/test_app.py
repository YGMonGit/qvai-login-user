import pytest
from .app import lambda_handler  # Import your Lambda function

def test_lambda_returns_200_with_valid_api_key():
    # Simulate a valid API Gateway event with API key
    event = {
        "httpMethod": "GET",
        "headers": {
            "x-api-key": "VALID_KEY"  # This key won't match AWS yet
        }
    }
    
    response = lambda_handler(event, None)
    
    # This test will FAIL because the Lambda doesn't check the API key yet
    assert response["statusCode"] == 200  # <--- Will fail

def test_lambda_returns_403_without_api_key():
    # Simulate a request without API key
    event = {
        "httpMethod": "GET",
        "headers": {}
    }
    
    response = lambda_handler(event, None)
    
    # This test will FAIL because the Lambda doesn't validate the API key
    assert response["statusCode"] == 403  # <--- Will fail