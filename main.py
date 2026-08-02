from fastapi import FastAPI
from app.resources.routes import routers as personal_routes


app = FastAPI()

@app.get("/",status_code=200)
async def health_check():
    return {"message": "Ok, funcionando"}

app.include_router(router=personal_routes)