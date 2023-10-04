from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.post("/signup")
def signup():
  return {"msg": "registering..."}

@auth_router.post("/signin")
def signin():
  return {"msg": "logging..."}

