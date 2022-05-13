from pymongo import MongoClient


def connect_db():
    db_pass = "toor"
    db_user = "root"
    db_address = "localhost"
    db_path = "/?authMechanism=DEFAULT"
    uri = f"mongodb://{db_user}:{db_pass}@{db_address}:27017{db_path}"

    client = MongoClient(uri)
    db = client["burnrecon"]
    return db
