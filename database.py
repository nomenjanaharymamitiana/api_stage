import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Force l'utilisation de la variable propre de l'interface Render en production
if os.getenv("RENDER"):
    DATABASE_URL = os.getenv("DATABASE_URL")
else:
    # En local : lit le .env local
    DATABASE_URL = os.getenv("DATABASE_URL")

# Si pour une raison quelconque DATABASE_URL reste vide ou invalide
if not DATABASE_URL or "@" not in DATABASE_URL:
    DATABASE_URL = "postgresql://postgres:allerenavant@localhost:5433/ged_db"

# Nettoyage des espaces blancs accidentels
DATABASE_URL = DATABASE_URL.strip()

# Correction du préfixe SQLAlchemy
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Vérification et injection de sécurité pour le port si Render a tronqué l'URL
if os.getenv("RENDER") and ":5432" not in DATABASE_URL and "oregon-postgres" not in DATABASE_URL:
    # Recompose l'URL Render au format strict attendu par SQLAlchemy
    DATABASE_URL = "postgresql://stage_1lk6_user:jsfvbvlWNLkS417GXZ3NDxtQcekFqrfV@://render.com"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
