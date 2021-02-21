from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .dependencies import get_query_token, get_token_header
from .routers import user, text_rec
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

origins = [
    "http://api.spycehub.com",
    "https://api.spycehub.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(text_rec.router)

@app.get("/root/")
async def root():
    return 10