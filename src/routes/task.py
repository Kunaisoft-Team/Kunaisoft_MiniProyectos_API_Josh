from fastapi              import APIRouter, Response, status
from re                   import match

from src.utils.constants  import TASKS_ROUTE, MONGO_ID_REGEX
from src.models.Task      import Task

task_router = APIRouter()

@task_router.get(TASKS_ROUTE)
async def get_tasks(res: Response, id: str = None):
  if id:
    if not match(MONGO_ID_REGEX, id):
      res.status_code = status.HTTP_400_BAD_REQUEST
      return {"msg": "Invalid ObjectID"}

    task = await Task.get_task_by_filter({"_id": id})
    
    if not task:
      res.status_code = status.HTTP_404_NOT_FOUND
      return {"msg": "Task not found"}

    task["_id"] = str(task["_id"])
    return {"task": task}
  
  tasks = await Task.get_tasks()
  for task in tasks:
    task["_id"] = str(task["_id"])
  return {"tasks": tasks}

@task_router.post(TASKS_ROUTE)
async def create(task: Task, res: Response):
  found_task = await Task.get_task_by_filter({"title": task.title})

  if found_task:
    res.status_code = status.HTTP_409_CONFLICT
    return {
    "msg": "The task already exists", 
    "error": True, 
    "task": task
  }

  created_task        = await Task.create_task(data=dict(task))
  created_task["_id"] = str(created_task["_id"])
  if not created_task: 
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {
      "msg": "Error trying to create the task", 
      "error": created_task, 
      "task": {}
    }

  res.status_code = status.HTTP_201_CREATED
  return {
    "msg": "Task created successfully!", 
    "error": False, 
    "task": created_task
  }

@task_router.put(TASKS_ROUTE)
async def update(res: Response, new_data: Task, id: str = None):
  if not new_data:
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"msg": "The new data's required"}
  
  if not match(MONGO_ID_REGEX, id):
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"msg": "Invalid ObjectID"}
  
  updated_task        = await Task.update_task(new_data, id)

  if not updated_task:
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"msg": "Error trying to update. Try again..."}
  
  updated_task["_id"] = str(updated_task["_id"])

  return {"msg": f"Task with id {id} updated successfully", "updated_task": updated_task}

@task_router.delete(TASKS_ROUTE)
async def delete(res: Response, id: str = None):
  if not match(MONGO_ID_REGEX, id):
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"msg": "Invalid ObjectID"}
  
  response = await Task.delete_task(id)
  print(response)

  if not response:
    res.status_code = status.HTTP_404_NOT_FOUND
    return {"msg": "Task not found"}

  return {"msg": f"Task with id {id} deleted successfully"}


