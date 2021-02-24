from dotenv import load_dotenv
from os.path import join, dirname
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .dependencies import get_query_token, get_token_header
from .routers import user, text_rec

app = FastAPI()

origins = [
    "*"
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