from src.utils.constants import EMAIL_REGEX
import re

def validate(data: dict, valid_data: list, update: bool = False):
  response    = {"error": False, "info": [], "status": 200}
  data_keys   = list(data.keys())

  if len(list(data)) == 0:
    response["error"]   = True
    response["status"]  = 400
    response["info"].append("The data can't be empty")
    return response
  
  if not update and data_keys != valid_data:
    response["error"]   = True
    response["status"]  = 400
    response["info"].append(f"Invalid data, excepted: {valid_data}")
    return response

  for key, value in data.items():  
    if type(value) != str:
      response["error"]   = True
      response["status"]  = 400
      response["info"].append(f"The {key} field must be text")

    elif key == "email" and not re.match(EMAIL_REGEX, value):
      response["error"]   = True
      response["status"]  = 400
      response["info"].append(f"The {key} field must be a valid email: example@gmail.com")

  return response