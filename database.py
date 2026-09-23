import os
from urllib.parse import urlsplit, urlunsplit

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Render et le développement local utilisent la même variable d'environnement.
DATABASE_URL = os.getenv("DATABASE_URL")

# Si pour une raison quelconque DATABASE_URL reste vide ou invalide
if not DATABASE_URL or "@" not in DATABASE_URL:
    DATABASE_URL = "postgresql://postgres:allerenavant@localhost:5433/ged_db"

# Nettoyage des espaces blancs accidentels
DATABASE_URL = DATABASE_URL.strip()

# Correction du préfixe SQLAlchemy
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Certaines configurations peuvent produire un port vide (par exemple `host:/db`).
# SQLAlchemy accepte l'absence de port, mais pas le séparateur `:` sans valeur.
parsed_url = urlsplit(DATABASE_URL)
if parsed_url.netloc.endswith(":"):
    DATABASE_URL = urlunsplit(
        parsed_url._replace(netloc=parsed_url.netloc[:-1])
    )

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
