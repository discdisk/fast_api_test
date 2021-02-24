from fastapi import APIRouter
from datetime import timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from ..models.user import User, Token, fake_users_db, SignUpParam, UserInDB, user_db, ObjectId
from ..services.auth import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_active_user, get_password_hash

router = APIRouter(prefix='/users', tags=['users'])
@router.get("/count/")
async def users_count():
    return 10


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]



@router.post("/sign_up", response_model=UserInDB)
async def sign_up(form_data: SignUpParam):
    newUser = UserInDB(
        # id=ObjectId(),
        **{**form_data.dict(), **{'hashed_password': get_password_hash(form_data.password) }})

    res = await user_db.insert_one(newUser.mongo())
    # assert res.inserted_id == newUser.id
    newUser.id = res.inserted_id
    return newUser.dict(exclude_none=True)

