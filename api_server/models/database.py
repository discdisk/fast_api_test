from motor.motor_asyncio import AsyncIOMotorClient
import os

db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
client = AsyncIOMotorClient(db_host)
db = client[db_name]