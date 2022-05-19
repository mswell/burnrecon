from pymongo import MongoClient
from burnrecon.config import settings


def connect_db():
    db_pass = settings.MONGO_DB_PASS
    db_user = settings.MONGO_DB_USER
    db_address = settings.database.address
    db_path = "/?authMechanism=DEFAULT"
    uri = f"mongodb://{db_user}:{db_pass}@{db_address}:27017{db_path}"

    client = MongoClient(uri)
    db = client["burnrecon"]
    return db
