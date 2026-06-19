from fastapi import APIRouter

auth_routes = APIRouter(prefix="/auth", tags=["auth"])

@auth_routes.get("/")
async def autenticate():
    """
    This is the standard authentication route of the system
    """
    return {"message": "You accessed the standard authentication route", "authenticated": False}
