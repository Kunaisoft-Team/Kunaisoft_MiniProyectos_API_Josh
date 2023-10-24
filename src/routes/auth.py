from fastapi              import APIRouter, HTTPException
from passlib.context      import CryptContext
from datetime             import timedelta

from src.models.Auth      import Auth
from src.models.Token     import Token
from src.utils.constants  import AUTH_ROUTE, TOKEN_EXPIRES_MINUTES

auth_router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@auth_router.post(AUTH_ROUTE)
async def signin(user_data: Auth):
  user, error, status = await Auth.authenticate_user(
    user_data.email,
    user_data.password,
    pwd_context
  )

  if not user:
    raise HTTPException(status_code=status, detail={"msg": error}, headers={"WWW-Authenticate": "Bearer"})

  token_data = {
    "id": user["_id"],
    "name": user["name"],
    "email": user["email"],
  }
  
  expires_in = timedelta(minutes=int(TOKEN_EXPIRES_MINUTES))
  
  token = Token.create_token(data=token_data, expires_in=expires_in)

  return {"access_token": token}

@auth_router.get(AUTH_ROUTE)
def get_user(access_token: str):
  current_user = Token.decode_token(access_token)
  if not current_user:
    raise HTTPException(status_code=401, detail={"msg": "Invalid token"})
  
  return current_user
