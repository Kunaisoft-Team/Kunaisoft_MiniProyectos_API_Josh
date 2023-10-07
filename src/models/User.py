from pydantic             import BaseModel, Field
from bson                 import ObjectId

from src.utils.db         import db
from src.utils.constants  import EMAIL_REGEX

class User(BaseModel):
  name: str     
  email: str    = Field(pattern=EMAIL_REGEX)
  password: str = Field(min_length=6)
  tasks: list   = []

  @classmethod
  async def get_users(self):
    cursor  = db.users.find()
    users   = [document async for document in cursor]
    return users

  @classmethod
  async def get_user_by_filter(self, filter):
    if filter.get("id"):
      user  = await db.users.find_one({"_id": ObjectId(id)})
    else:
      user  = await db.users.find_one(filter)
    return user  
  
  @classmethod
  async def create_user(self, data):
    new_user      = await db.users.insert_one(data)
    user_created  = await db.users.find_one({"_id": new_user.inserted_id})
    return user_created
    