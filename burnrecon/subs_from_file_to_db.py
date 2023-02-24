import datetime
import concurrent.futures

from database import connect_db
from pathlib import Path


dic_subdomain = {}


def setup_parser(target, line):
    db = connect_db()
    collection = db["subdomains"]
    dic_subdomain["target"] = target
    dic_subdomain["subdomain"] = line.rstrip("\n")
    data = {
        "target": dic_subdomain["target"],
        "subdomain": dic_subdomain["subdomain"],
        "date": datetime.datetime.utcnow(),
    }

    if collection.find_one({"subdomain": data["subdomain"]}):
        print("Document already exists")
    else:
        collection.insert_one(data)
        print("Document inserted")


def subs_from_file_parser(target, subs_file):
    filepath = Path(subs_file)
    with open(f"{filepath}", mode="r") as _file:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for line in _file:
                futures.append(
                    executor.submit(setup_parser, target, line=line.rstrip("\n"))
                )
