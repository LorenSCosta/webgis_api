from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.user.user_controller import router as user_router
from app.auth.auth_controller import router as auth_router
from app.property.property_controller import router as property_router
from app.typeUser.typeUser_controller import router as typeUser_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:53210",
    "http://127.0.0.1:53210",
    "http://localhost",
    "http://127.0.0.1",
    "*"  # apenas para desenvolvimento
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)        
app.include_router(typeUser_router)     
app.include_router(property_router)
app.include_router(user_router)


