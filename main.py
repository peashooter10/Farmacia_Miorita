import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ─── IMPORT ROUTERE ────────────────────────────────────
# pagini
from Routers.MainPage import main_page
from Routers.ManageCont.LoginCont import login
from Routers.ContFarmaciaMiorita.PaginaPrincipala import cont
from Routers.ContFarmaciaMiorita.Sectiuni.Administrare.Angajati import angajati

# pe viitor:
# from Routers.ContFarmaciaMiorita.Sectiuni.Administrare.Sesizari import sesizari

app = FastAPI()

# ─── MIDDLEWARE ────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── STATIC FILES ──────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "Frontend")
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

# ─── ROUTERE ───────────────────────────────────────────
app.include_router(main_page.router)
app.include_router(login.router)
app.include_router(cont.router)
app.include_router(angajati.router)

# pe viitor:
# app.include_router(sesizari.router)