from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum  # 1. Ajoutez cette importation

import models
from database import engine
from routes import auth_router, document_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="GED Haute Matsiatra - API DAG/RH", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(document_router)

@app.get("/")
def root():
    return {"message": "API GED Haute Matsiatra fonctionnelle"}

# 2. Ajoutez cette ligne tout à la fin de votre fichier
handler = Mangum(app)
