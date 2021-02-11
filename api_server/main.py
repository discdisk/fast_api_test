import mq_task.mq_task as tasks
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import asyncio
version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ImgURI(BaseModel):
    imgURI: str


@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}


@app.post("/hand_written_digit")
async def hand_written_digit(imgURI: ImgURI):
    task = tasks.rec_digit.delay(imgURI.imgURI)
    while not task.ready():
        await asyncio.sleep(1)
    return str(task.result)
