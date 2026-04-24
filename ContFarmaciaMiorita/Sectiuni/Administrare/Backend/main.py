from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from database import SessionLocal
import models

# creez aplicatia fastapi
app = FastAPI()

# permit frontend-ului sa faca request-uri
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # permit orice origine (pentru test)
    allow_methods=["*"],
    allow_headers=["*"],
)

# modelul datelor primite din frontend
class CreareAngajat(BaseModel):
    nume: str
    prenume: str
    email: str
    localitate: str
    judet: str
    rol: str


# test daca merge api-ul
@app.get("/")
def root():
    return {"message": "API is running"}


# get - iau angajatii din baza de date
@app.get("/angajati")
def get_angajati(sort_by: Optional[str] = "id", order: Optional[str] = "asc"):

    db = SessionLocal()  # deschid conexiunea la baza de date

    try:
        # campuri valide pentru sortare
        allowed_fields = {"id", "nume", "prenume", "email", "localitate", "judet","rol"}

        if sort_by not in allowed_fields:
            raise HTTPException(status_code=400, detail="Câmp invalid")

        # aleg coloana dupa care sortam
        column = getattr(models.Angajat, sort_by)

        # iau datele din tabela Employee
        query = db.query(models.Angajat)

        # sortez datele
        query = query.order_by(column.desc() if order == "desc" else column.asc())

        # trimit rezultatul la frontend(js)
        return query.all()

    finally:
        db.close()  # inchid conexiunea


# post - adaug angajati in baza de date
@app.post("/angajati")
def add_angajat(emp: CreareAngajat):

    db = SessionLocal() 

    try:
        # creez obiectul pentru baza de date
        new_emp = models.Angajat(**emp.dict())

        # salvez obiectul in baza de date
        db.add(new_emp)
        db.commit()
        db.refresh(new_emp)

        # raspuns catre frontend ca am adaugat angajatul
        return {"message": "Angajat adăugat", "id": new_emp.id}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()


# delete - sterg angajatul din baza de date
@app.delete("/angajati/{emp_id}")
def delete_angajat(emp_id: int):

    db = SessionLocal()

    try:
        # cautam angajatul dupa id
        emp = db.query(models.Angajat).filter(models.Angajat.id == emp_id).first()

        if not emp:
            raise HTTPException(status_code=404, detail="Angajat negăsit")

        # sterg angajatul din baza de date
        db.delete(emp)
        db.commit()

        return {"message": f"Angajat {emp_id} șters"}

    finally:
        db.close()
