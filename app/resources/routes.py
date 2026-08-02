from fastapi import APIRouter,status
from .schemas import InstanceRequest
from .services import new_instance,get_instance,delete_instance


routers = APIRouter()

@routers.post("/instances", 
            status_code=status.HTTP_201_CREATED,
            )
async def create_instance(data: InstanceRequest):
    response = new_instance(data)
    return response

@routers.get("/instances/{instance_id}")
async def get_instance_route(instance_id:str):
    response = get_instance(instance_id)
    return response

@routers.delete("/instances/{instance_id}")
async def delete_instance_route(instance_id:str):
    response = delete_instance(instance_id)
    return response