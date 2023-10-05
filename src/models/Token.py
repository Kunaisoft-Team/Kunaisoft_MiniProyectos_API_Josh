from datetime             import timedelta
from jose                 import JWTError, jwt
from datetime             import datetime

from src.utils.today      import get_current_date
from src.utils.constants  import SECRET_KEY

class Token():
  @classmethod
  def create_token(self, data: dict, expires_in: timedelta = None):
    print(expires_in)
    if not expires_in:
      expire = datetime.utcnow() + timedelta(minutes=15)
    else:
      expire = datetime.utcnow() + expires_in

    print(expire)

    data.update({"exp": expire})
    token = jwt.encode(data, SECRET_KEY)
    return token
  
  @classmethod
  def decode_token(self, token: str):
    try:
      result = jwt.decode(token, SECRET_KEY)
      return result.get("sub")
    except JWTError:
      return False
