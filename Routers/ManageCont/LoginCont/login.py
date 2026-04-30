import os
from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

FRONTEND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "Frontend")

@router.get("/login")
def login_page():
    return FileResponse(os.path.join(FRONTEND_DIR, "ManageCont/LoginCont/UserLogin.html"))