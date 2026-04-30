from sqlalchemy import Column, Integer, String
from database import Base, engine

# clasa angajat are aceeasi structura ca si tabela din baza de date
class Angajat(Base):
    __tablename__ = "angajati"
    id = Column(Integer, primary_key=True, index=True)
    nume = Column(String(100))
    prenume = Column(String(100))
    email = Column(String(100))
    localitate = Column(String(100))
    judet = Column(String(100))
    rol = Column(String(100))
    varsta = Column(String(10))

Base.metadata.create_all(bind=engine)