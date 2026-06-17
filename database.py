from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Création de la base de données SQLite
engine = create_engine("sqlite:///qualiopilot.db", echo=False)
Base = declarative_base()

# Table des documents
class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    nom_fichier = Column(String(255), nullable=False)
    type_fichier = Column(String(50))
    date_import = Column(DateTime, default=datetime.now)
    chemin = Column(String(500))

# Table des textes extraits
class Texte(Base):
    __tablename__ = "textes"
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, nullable=False)
    contenu = Column(Text)
    date_extraction = Column(DateTime, default=datetime.now)

# Table des analyses IA
class Analyse(Base):
    __tablename__ = "analyses"
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, nullable=False)
    resultat = Column(Text)
    date_analyse = Column(DateTime, default=datetime.now)

# Création des tables dans la base
def initialiser_base():
    Base.metadata.create_all(engine)
    print("Base de données créée avec succès.")

# Obtenir une session
def get_session():
    Session = sessionmaker(bind=engine)
    return Session()

# Test
if __name__ == "__main__":
    initialiser_base()