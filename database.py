import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Récupère l'URL (du .env en local ou de Render en production)
DATABASE_URL = os.getenv("DATABASE_URL")

# Si DATABASE_URL n'existe pas du tout, utilise le localhost par défaut
if not DATABASE_URL:
    DATABASE_URL = "postgresql://postgres:allerenavant@localhost:5433/ged_db"

# Sécurité imposée par SQLAlchemy (remplace postgres:// par postgresql://)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Configuration de l'engine standard de SQLAlchemy 2.0
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
