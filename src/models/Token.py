from datetime             import timedelta
from jose                 import JWTError, jwt
from datetime             import datetime

from src.utils.constants  import SECRET_KEY

class Token:
  @classmethod
  def create_token(self, data: dict, expires_in: timedelta = None):
    if not expires_in:
      expire = datetime.utcnow() + timedelta(minutes=15)
    else:
      expire = datetime.utcnow() + expires_in

    data.update({"exp": expire})
    token = jwt.encode(data, SECRET_KEY)
    return token
  
  @classmethod
  def decode_token(self, token: str):
    try:
      result = jwt.decode(token, SECRET_KEY)
      return result
    except JWTError:
      return False
