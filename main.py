import models
from database import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth_router, document_router

# Vous pouvez réactiver cette ligne sur Render !
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
