from sqlalchemy import Column, Integer, String
from database import Base, engine

# clasa angajat are aceeasi structura ca si tabela mea de angajati din baza de date
class Angajat(Base):
    __tablename__ = "angajati" # numele tabelei
    id = Column(Integer, primary_key=True, index=True)
    nume = Column(String(100))
    prenume = Column(String(100))
    email = Column(String(100))
    localitate = Column(String(100))
    judet = Column(String(100))
    rol = Column(String(100))

class Utilizator(Base):
    __tablename__="utilizator"
    id=Column(Integer,primary_key=True,index=True)
    nume = Column(String(100))
    prenume = Column(String(100))
    id_localitate=Column(Interger)
    id_email=Column(Interger)
    id_rol=Column(Interger)
    id_comenzi=Column(Interger)

class 

Base.metadata.create_all(bind=engine) # creez baza de date