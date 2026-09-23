import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# 1. Si l'application s'exécute sur Render, on force l'URL réseau valide avec le port 5432
if os.getenv("RENDER"):
    DATABASE_URL = "postgresql://stage_1lk6_user:jsfvbvlWNLkS417GXZ3NDxtQcekFqrfV@://render.com"
else:
    # 2. En local sur votre machine, il utilisera votre configuration par défaut
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:allerenavant@localhost:5433/ged_db")

# Nettoyage et correction obligatoires du préfixe requis par SQLAlchemy
DATABASE_URL = DATABASE_URL.strip()
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
