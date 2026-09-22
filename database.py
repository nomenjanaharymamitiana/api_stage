import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Charge le fichier .env si vous êtes en développement local
from dotenv import load_dotenv

load_dotenv()

# Par défaut, utilise votre base locale. Sur Vercel, il lira la variable DATABASE_URL.
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:allerenavant@localhost:5433/ged_db"
)

# Sécurité : Vercel/Supabase utilisent parfois "postgres://", SQLAlchemy exige "postgresql://"
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dépendance pour obtenir la session de BDD dans les routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
