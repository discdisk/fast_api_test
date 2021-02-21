from fastapi import APIRouter
router = APIRouter(prefix='/text_rec', tags=['text_rec'])

@router.post("/")
async def text_rec():
    """
    hand write digit
    """
    return 10
