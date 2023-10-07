from fastapi              import APIRouter, HTTPException, Response, status
from passlib.context      import CryptContext
from re                   import match

from src.utils.constants  import USERS_ROUTE, MONGO_ID_REGEX
from src.models.User      import User

user_router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@user_router.post(USERS_ROUTE)
async def signup(user: User, res: Response):
  found_user = await User.get_user_by_filter({"email": user.email})

  if found_user:
    raise HTTPException(status_code=409, detail={"msg": "The user already exists"})
  
  user.password = pwd_context.hash(user.password)

  created_user = await User.create_user(data=dict(user))
  
  if not created_user:
    raise HTTPException(status_code=400, detail={"msg": "Error trying to create the user"})
  
  created_user["_id"] = str(created_user["_id"])

  res.status_code = status.HTTP_201_CREATED
  return {
    "msg": "User created successfully!", 
    "user": created_user
  }

@user_router.get(USERS_ROUTE)
async def get_users(id: str = None):
  if id:
    if not match(MONGO_ID_REGEX, id):
      raise HTTPException(status_code=400, detail={"msg": "Invalid ObjectID"})

    user = await User.get_user_by_filter({"_id": id})
    
    if not user:
      raise HTTPException(status_code=400, detail={"msg": "User not found"})

    user["_id"] = str(user["_id"])
    return {"user": user}

  users = await User.get_users()

  for user in users:
    user["_id"] = str(user["_id"])
  return {"users": users}