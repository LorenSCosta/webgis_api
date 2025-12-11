from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from app.user.user_controller import router as user_router
from app.auth.auth_controller import router as auth_router
from app.property.property_controller import router as property_router
from app.typeUser.typeUser_controller import router as typeUser_router

# -------------------------
# Detecta ambiente
# -------------------------
APP_PROFILE = os.getenv("APP_PROFILE", "DEV")  # Por padrão DEV, altere no Render para PROD

app = FastAPI(title="WebGIS API")

# -------------------------
# Configuração CORS
# -------------------------
if APP_PROFILE == "PROD":
    origins = [
        "https://seu-frontend.vercel.app",
        "https://seu-frontend.netlify.app",
        
    ]
else:
    origins = [
        "http://localhost:53210",
        "http://127.0.0.1:53210",
        "http://localhost",
        "http://127.0.0.1",
        "*"  # apenas para desenvolvimento
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://webgis-api.onrender.com", "https://webgis-qvd0v9pmm-lorenscostas-projects.vercel.app", "https://webgis-front.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Routers
# -------------------------
app.include_router(auth_router)
app.include_router(typeUser_router)
app.include_router(property_router)
app.include_router(user_router)


