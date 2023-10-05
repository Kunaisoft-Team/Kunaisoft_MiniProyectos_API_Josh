from src.utils.constants import MONGO_URI
from motor.motor_asyncio import AsyncIOMotorClient

def connect_to_db():
  try:
    client  = AsyncIOMotorClient(MONGO_URI)
    db      = client.tasks_app_db
    return db
  except Exception as err:
    print("ERROR TRYING TO CONNECT")
    print(err)
    return False
