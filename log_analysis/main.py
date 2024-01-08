from fastapi import FastAPI
from .routes import log_routes
from dotenv import load_dotenv
from .config.db_config import DatabaseConnector
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

DatabaseConnector.initialize_connection()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

app.include_router(log_routes.router)
