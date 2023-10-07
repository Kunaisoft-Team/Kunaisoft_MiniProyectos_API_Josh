from dotenv import load_dotenv
from os     import getenv 

load_dotenv()

TASKS_ROUTE           = getenv("TASKS_ROUTE")
USERS_ROUTE           = getenv("USERS_ROUTE")
AUTH_ROUTE            = getenv("AUTH_ROUTE")

MONGO_URI             = getenv("MONGO_URI")
CLIENT_URL            = getenv("CLIENT_URL")

SECRET_KEY            = getenv("SECRET_KEY")
TOKEN_EXPIRES_MINUTES = getenv("TOKEN_EXPIRES_MINUTES")

EMAIL_REGEX   = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"

JWT_REGEX     = r"^([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_\-\+\/=]*)"

MONGO_ID_REGEX = r"(?:[0-9a-f]{24})"