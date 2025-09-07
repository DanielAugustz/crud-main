from fastapi import FastAPI
from app.routers import alunos

app = FastAPI(title="CRUD MongoDB")

app.include_router(alunos.router)

@app.get("/")
def home():
    return {"message": "Bem-vindo ao CRUD MongoDB com FastAPI"}
