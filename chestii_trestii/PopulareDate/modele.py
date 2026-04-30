from sqlalchemy import Column, Integer, String, ForeignKey
from baza_de_date import Base, engine

# clasa angajat are aceeasi structura ca si tabela mea de angajati din baza de date
class Angajati(Base):
    __tablename__ = "Angajati" # numele tabelei
    id_angajat = Column(Integer, primary_key=True, index=True)
    id_nume = Column(Integer)
    id_prenume = Column(Integer)
    id_farmacie = Column(Integer, ForeignKey("Farmacii.id_farmacie"))

class Farmacii(Base):
    __tablename__ = "Farmacii"
    id_farmacie = Column(Integer,primary_key=True,index=True)
    denumire = Column(String(100))
    adresa = Column(String(100))
    id_localitate = Column(Integer, ForeignKey("Localitate.id_localitate"))
    id_email = Column(Integer, ForeignKey("Email.id_email"))

class StocFarmacie(Base):
    __tablename__ = "StocFarmacie"
    id_stoc = Column(Integer,primary_key=True,index=True)
    id_farmacie = Column(Integer, ForeignKey("Farmacii.id_farmacie"))
    id_medicament = Column(Integer, ForeignKey("Medicamente.id_medicamente"))
    pret_achizitie = Column(Integer)
    pret_vanzare = Column(Integer)

class Categorii(Base):
    __tablename__ = "Categorii"
    id_categorie= Column(Integer,primary_key=True,index=True)
    categorie = Column(String(100))

class Medicamente(Base):
    __tablename__ = "Medicamente"
    id_medicamente = Column(Integer,primary_key=True,index=True)
    denumire = Column(String(100))
    id_categorie = Column(Integer, ForeignKey("Categorii.id_categorie"))
    id_furnizor = Column(Integer, ForeignKey("Partener.id_partener"))

class Judet(Base):
    __tablename__ = "Judet"
    id_judet = Column(Integer, primary_key=True, index=True)
    judet = Column(String(100))

class Localitate(Base):
    __tablename__ = "Localitate"
    id_localitate= Column(Integer,primary_key=True,index=True)
    localitate = Column(String(100))
    id_judet = Column(Integer, ForeignKey("Judet.id_judet"))

class Utilizatori(Base):
    __tablename__ = "Utilizatori"
    id_utilizator = Column(Integer,primary_key=True,index=True)
    nume = Column(String(100))
    prenume = Column(String(100))
    adresa = Column(String(100))
    id_email = Column(Integer, ForeignKey("Email.id_email"))
    id_localitate = Column(Integer, ForeignKey("Localitate.id_localitate"))
    id_judet = Column(Integer, ForeignKey("Judet.id_judet"))
    id_rol = Column(Integer, ForeignKey("Roluri.id_rol"))

class Roluri(Base):
    __tablename__ = "Roluri"
    id_rol = Column(Integer,primary_key=True,index=True)
    rol = Column(String(100))

class Email(Base):
    __tablename__ = "Email"
    id_email = Column(Integer,primary_key=True,index=True)
    email = Column(String(100))

class Vanzari(Base):
    __tablename__ = "Vanzari"
    id_vanzare = Column(Integer,primary_key=True,index=True)
    id_partener = Column(Integer, ForeignKey("Partener.id_partener"))
    id_farmacie = Column(Integer, ForeignKey("Farmacii.id_farmacie"))

class VanzariDetalii(Base):
    __tablename__ = "VanzariDetalii"
    id_detaliiVanzare = Column(Integer,primary_key=True,index=True)
    id_medicament = Column(Integer, ForeignKey("Medicamente.id_medicamente"))
    id_stoc = Column(Integer, ForeignKey("StocFarmacie.id_stoc"))
    id_vanzare = Column(Integer, ForeignKey("Vanzari.id_vanzare"))
    cantitate = Column(Integer)
    pret = Column(Integer)

class Partener(Base):
    __tablename__ = "Partener"
    id_partener = Column(Integer,primary_key=True,index=True)
    denumire = Column(String(100))
    adresa = Column(String(100))
    id_localitate = Column(Integer, ForeignKey("Localitate.id_localitate"))
    id_judet = Column(Integer, ForeignKey("Judet.id_judet"))
    id_email = Column(Integer, ForeignKey("Email.id_email"))
    tipPartener = Column(String(100))

class Retete(Base):
    __tablename__ = "Retete"
    id_reteta = Column(Integer,primary_key=True,index=True)
    id_partener = Column(Integer, ForeignKey("Partener.id_partener"))
    id_farmacie = Column(Integer, ForeignKey("Farmacii.id_farmacie"))

class ReteteDetalii(Base):
    __tablename__ = "ReteteDetalii" 
    id_detaliiReteta = Column(Integer, primary_key=True)
    id_medicament = Column(Integer, ForeignKey("Medicamente.id_medicamente"))
    id_stoc = Column(Integer, ForeignKey("StocFarmacie.id_stoc"))
    id_reteta = Column(Integer, ForeignKey("Retete.id_reteta"))

Base.metadata.create_all(bind=engine) # creez baza de date