import pytest
from .app import lambda_handler  # Import your Lambda function

def test_lambda_with_correct_credentials():
    event = {
        "username": "admin",
        "password": "password123"
    }
    
    response = lambda_handler(event, None)
    
    # This test will Pass because the Lambda return status 200 for correct credential
    assert response["statusCode"] == 200  # <--- Will fail

def test_lambda_with_incorrect_username():
    event = {
        "username": "root",
        "password": "password123"
    }
    
    response = lambda_handler(event, None)
    
    # This test will pass because the Lambda function will give 401 for wrong credential
    assert response["statusCode"] == 401  # <--- Will fail