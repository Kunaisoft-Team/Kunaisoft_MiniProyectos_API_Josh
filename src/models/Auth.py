from pydantic     import BaseModel, Field

from src.utils.db import db

class Auth(BaseModel):
  email: str
  password: str = Field(min_length=6)

  @classmethod
  async def __validate_user__(self, email):    
    user = await db.users.find_one({"email": email})
    
    if not user:
      return None
    
    for index, task_id in enumerate(user["tasks"]):
      user["tasks"][index] = str(task_id)
    
    return user
  
  @classmethod
  def __validate_password__(self, password, hashed_password, pwd_context):
    return pwd_context.verify(password, hashed_password)

  @classmethod
  async def authenticate_user(self, email, password, pwd_context):
    user = await self.__validate_user__(email)

    if not user:
      return False, "User not found", 404
    
    user["_id"] = str(user["_id"])

    match_password = self.__validate_password__(password, user["password"], pwd_context)
    if not match_password:
      return False, "The passwords doesn't match", 401
    
    return user, None, 200