import logging
import json

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
  """
    Providing specific error messages like "User not found" or "Wrong password" in an authentication system is a bad practice. 
    This can help attackers guess valid usernames or passwords by testing different inputs. 

    To improve security, it's better to use a general message like "Incorrect credentials" 
    so that attackers can't tell whether the username or password is wrong.
  """
  try:
    username = event.get("username")
    password = event.get("password")

    if not username or not password:
      return {
        "statusCode": 400,
        "body": json.dumps({"message": "Failure: Missing username or password."}),
      }
  except KeyError as error: #This for missing key exception
    return {
      "statusCode": 500,
      "body": json.dumps({"message": f"Failure: Missing key {str(error)} in request."})
    }
  except Exception as error: #This for every other exception that might occur
    return {
      "statusCode": 500,
      "body": json.dumps({"message": "Failure: An unexpected error occurred"})
    }

  # Log the login attempt
  log_data = {
    "event": "login_attempt",
    "username": username,
    "status": "success" if username == "admin" and password == "password123" else "failed"
  }
  logger.info(json.dumps(log_data))  # Ensure JSON format in logs

  if username == "admin" and password == "password123":
    return {
      "statusCode": 200,
      "body":json.dumps({"message": "Login successful!"})
    }
  else:
    return {
      "statusCode": 401,
      "body": json.dumps({"message": "Login failed. Invalid credentials."})
    }