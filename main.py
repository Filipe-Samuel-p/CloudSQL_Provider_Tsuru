from fastapi import FastAPI
from app.resources.schemas import User

app = FastAPI()

@app.get("/",status_code=200)
async def health_check():
    return {"message": "Ok, funcionando"}

