from src.utils.db import connect_to_db

from pydantic import BaseModel

class Task(BaseModel):
  id: str
  name: str
  description: str
  completed: bool = False

  @classmethod
  async def get_tasks(self):
    db      = connect_to_db()
    cursor  = db.tasks.find()
    tasks   = [document async for document in cursor]
    return tasks
  
  @classmethod
  async def get_task(self, id):
    db    = connect_to_db()
    task  = await db.tasks.find_one({"_id": id})
    return task
  
  @classmethod
  async def create_task(self, data):
    db            = connect_to_db()
    new_task      = await db.tasks.insert_one(data)
    created_task  = await db.tasks.find_one({"_id": new_task.inserted_id})
    return created_task
  
  @classmethod
  async def update_task(self, new_data, id: str):
    db            = connect_to_db()
    await db.tasks.update_one({"_id": id}, {"$set": new_data})
    updated_task  = await db.tasks.find_one({"_id": id})
    return updated_task 
  
  @classmethod
  async def delete_task(self, id):
    db      = connect_to_db()
    result  = await db.tasks.delete_one({"_id": id})
    return result
  
