from src.utils.db import connect_to_db

class User:
  def __init__(self, name: str, email: str, password: str):
    self.name     = name
    self.email    = email
    self.password = password

  @classmethod
  async def get_user(self, id):
    db    = connect_to_db()
    user  = await db.users.find_one({"_id": id})
    return user
  
  @classmethod
  async def insert_user(self, data):
    db            = connect_to_db()
    user_created  = await db.users.insert_one(data)
    return user_created
    