from fastapi import APIRouter
from ..mq_task.mq_task import rec_digit
router = APIRouter(prefix='/text_rec', tags=['text_rec'])

from pydantic import BaseModel
class image(BaseModel):
    imgURI: str

@router.post("/")
async def text_rec(img: image):
    """
    hand write digit
    """
    res = rec_digit(img.imgURI)
    return res
