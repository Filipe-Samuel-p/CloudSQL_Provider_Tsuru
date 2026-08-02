from typing import Annotated

from fastapi import APIRouter,status, Depends, HTTPException, Form
from .schemas import InstanceRequest
from .services import new_instance,get_instance,delete_instance
from app.auth.auth import get_current_user


routers = APIRouter()

@routers.post("/resources",
            status_code=status.HTTP_201_CREATED,
            )
async def create_instance(data: Annotated[InstanceRequest, Form()], current_user = Depends(get_current_user)):

    if not current_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    response = new_instance(data)
    return response

@routers.get("/resources/{instance_id}")
async def get_instance_route(instance_id:str, current_user = Depends(get_current_user)):

    if not current_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    response = get_instance(instance_id)
    return response

@routers.delete("/resources/{instance_id}",)
async def delete_instance_route(instance_id:str, current_user = Depends(get_current_user)):
    if not current_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    response = delete_instance(instance_id)
    return response