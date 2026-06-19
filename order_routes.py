from fastapi import APIRouter

order_routes = APIRouter(prefix="/orders", tags=["orders"])

@order_routes.get("/list")
async def orders():
    """
     This is the standard route of system orders. All the routes of orders must be authenticated
    """
    return {"message": " You accessed the orders route"}