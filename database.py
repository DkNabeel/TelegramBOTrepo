from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client["movie_bot"]

files = db["files"]
users = db["users"]
requests = db["requests"]