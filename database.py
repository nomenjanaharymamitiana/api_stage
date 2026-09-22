import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Par défaut, utilise votre base locale.
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:allerenavant@localhost:5433/ged_db"
)

# Correction du préfixe exigé par SQLAlchemy
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Configuration de la connexion sécurisée
# Tous les arguments spécifiques à Supabase/Psycopg2 vont dans connect_args
connect_arguments = {}
if "supabase.co" in DATABASE_URL:
    connect_arguments["sslmode"] = "require"
    connect_arguments["prepared_statement_cache_size"] = 0

engine = create_engine(
    DATABASE_URL, 
    connect_args=connect_arguments
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dépendance pour obtenir la session de BDD dans les routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
