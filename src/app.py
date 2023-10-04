from fastapi import FastAPI

from src.routes.auth import auth_router
from src.routes.task import task_router

def init_app():
  app = FastAPI()

  app.include_router(auth_router)
  app.include_router(task_router)

  return app

