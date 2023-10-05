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

  expires_in = timedelta(minutes=int(TOKEN_EXPIRES_MINUTES))
  
  token = Token.create_token(data=user, expires_in=expires_in)


  return {"access-token": token}