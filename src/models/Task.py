from pydantic         import BaseModel
from bson             import ObjectId

from src.utils.db     import connect_to_db
from src.utils.today  import get_current_date

class Task(BaseModel):
  title: str
  description: str = None
  completed: bool = False
  created_at: str = get_current_date()
  updated_at: str = get_current_date()

  @classmethod
  async def get_tasks(self):
    db      = connect_to_db()
    cursor  = db.tasks.find()
    tasks   = [document async for document in cursor]
    return tasks
  
  @classmethod
  async def get_task_by_filter(self, filter: dict):
    db    = connect_to_db()
    if(filter.get("_id")):
      task  = await db.tasks.find_one({"_id": ObjectId(filter.get("_id"))})
    else:
      task  = await db.tasks.find_one(filter)
    return task
  
  @classmethod
  async def create_task(self, data: dict):
    db            = connect_to_db()
    new_task      = await db.tasks.insert_one(data)
    created_task  = await db.tasks.find_one({"_id": new_task.inserted_id})
    return created_task
  
  @classmethod
  async def update_task(self, new_data, id: str):
    db            = connect_to_db()
    new_data = { key:value for key, value in new_data.dict().items() if value is not None }
    await db.tasks.find_one_and_update({"_id": ObjectId(id)}, {"$set": new_data})
    updated_task  = await db.tasks.find_one({"_id": ObjectId(id)})
    return updated_task 
  
  @classmethod
  async def delete_task(self, id: str):
    db      = connect_to_db()
    result  = await db.tasks.find_one_and_delete({"_id": ObjectId(id)})
    return result
  
