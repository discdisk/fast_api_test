from .database import db, MongoModel, ObjectId, OID
from pydantic import BaseModel, Field
from typing import Optional
user_db = db['user']
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

class Token(MongoModel):
    access_token: str
    token_type: str


class TokenData(MongoModel):
    username: Optional[str] = None


class User(MongoModel):
    id: Optional[OID] = Field(description="User id")
    username: str = Field()
    email: Optional[str] = Field()
    full_name: Optional[str] = Field()
    disabled: Optional[bool] = Field()

class SignUpParam(MongoModel):
    username: str
    email: str
    password: str

class UserInDB(User):
    hashed_password: str = Field()


