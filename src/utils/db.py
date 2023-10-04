from src.utils.constants import MONGO_URI
from motor.motor_asyncio import AsyncIOMotorClient

def connect_to_db():
  client  = AsyncIOMotorClient(MONGO_URI)
  db      = client.tasks_app_db
  return db
