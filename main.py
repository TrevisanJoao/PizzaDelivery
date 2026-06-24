from idlelib.parenmatch import ParenMatch
from pickle import GET
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

from fastapi import FastAPI
from sqlalchemy.orm.loading import PostLoad
app = FastAPI()

bcrypt_context = CryptContext(schemes="bcrypt", deprecated="auto")

from auth_routes import auth_routes
from order_routes import order_routes

app.include_router(auth_routes)
app.include_router(order_routes)








# to run the application go to terminal and run command: uvicorn main:app --reload

# endpoint:
# /orders/create (path)

#Rest APIs
#GET -> read/get
#Post -> send/create
#Put/Patch -> edition
#Delete -> delete