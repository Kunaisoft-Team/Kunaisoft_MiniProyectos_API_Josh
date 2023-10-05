from fastapi import FastAPI

from src.routes.auth import auth_router
from src.routes.task import task_router
from src.routes.user import user_router

def init_app():
  app = FastAPI()

  app.include_router(auth_router)
  app.include_router(task_router)
  app.include_router(user_router)

  return app

