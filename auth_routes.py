from xml import dom
from fastapi import APIRouter, Depends, HTTPException
from models import User, db
from depencencies import get_session
from main import bcrypt_context
from schemas import UserSchema
from sqlalchemy.orm import Session


auth_routes = APIRouter(prefix="/auth", tags=["auth"])

@auth_routes.get("/")
async def autenticate():
    """
    This is the standard authentication route of the system
    """
    return {"message": "You accessed the standard authentication route", "authenticated": False}

@auth_routes.post("/create_account")
async def create_account(UserSchema: UserSchema, session = Depends(get_session)):
    user = session.query(User).filter(User.email==UserSchema.email).first()
    if user:
        raise HTTPException(status_code=400, details= "Email is already being used")
    else:
        encrypted_password = bcrypt_context.hash(UserSchema.passwrod)
        new_user = User(UserSchema.name, UserSchema.email, encrypted_password, UserSchema.active, UserSchema.admin)
        session.add(new_user)
        session.commit()
        return {"message": f" User created with success {new_user.email}"}