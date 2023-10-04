from fastapi              import APIRouter
from typing               import Union
from src.utils.constants  import TASKS_ROUTE

task_router = APIRouter()

@task_router.get(TASKS_ROUTE)
def get_all():
  return {"msg": "getting the tasks..."}

@task_router.get(TASKS_ROUTE)
def get_one(id: Union[str, None]):
  return {"msg": f"getting the task {id}"}

@task_router.post(TASKS_ROUTE)
def create(id: Union[str, None]):
  return {"msg": f"creating the task {id}"}

@task_router.put(TASKS_ROUTE)
def update(id: Union[str, None]):
  return {"msg": f"updating the task {id}"}

@task_router.delete(TASKS_ROUTE)
def delete(id: Union[str, None]):
  return {"msg": f"deleting the task {id}"}


