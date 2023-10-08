from src.utils.constants import MONGO_URI
from motor.motor_asyncio import AsyncIOMotorClient

try:
  client  = AsyncIOMotorClient(MONGO_URI)
  db      = client.tasks_app_db
except Exception as err:
  print(err)
