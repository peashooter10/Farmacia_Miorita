import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from database import SessionLocal
import models

router = APIRouter()

FRONTEND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "..", "Frontend")

@router.get("/angajati-page")
def angajati_page():
    return FileResponse(os.path.join(FRONTEND_DIR, "ContFarmaciaMiorita/Sectiuni/Administrare/Angajati/Angajati.html"))

class CreareAngajat(BaseModel):
    nume: str
    prenume: str
    email: str
    localitate: str
    judet: str
    rol: str
    varsta: str

@router.get("/angajati")
def get_angajati():
    db = SessionLocal()
    try:
        return db.query(models.Angajat).all()
    finally:
        db.close()

@router.post("/angajati")
def add_angajat(emp: CreareAngajat):
    db = SessionLocal()
    try:
        new_emp = models.Angajat(**emp.dict())
        db.add(new_emp)
        db.commit()
        db.refresh(new_emp)
        return {"message": "Angajat adăugat", "id": new_emp.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@router.delete("/angajati/{emp_id}")
def delete_angajat(emp_id: int):
    db = SessionLocal()
    try:
        emp = db.query(models.Angajat).filter(models.Angajat.id == emp_id).first()
        if not emp:
            raise HTTPException(status_code=404, detail="Angajat negăsit")
        db.delete(emp)
        db.commit()
        return {"message": f"Angajat {emp_id} șters"}
    finally:
        db.close()