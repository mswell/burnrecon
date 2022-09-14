import concurrent.futures
import os
import tempfile
from datetime import datetime
from pathlib import Path

from database import connect_db

random_name = tempfile.NamedTemporaryFile(delete=False)
final_file = Path(random_name.name)


def setup_naabu(subdomain):

    random_name = tempfile.NamedTemporaryFile(delete=False)
    naabu_out = Path(random_name.name)
    naabu_cmd = f"naabu -host {subdomain} -top-ports 100 -sa "
    naabu_cmd += f"-silent -o {naabu_out}"
    os.system(f"{naabu_cmd}")
    os.system(f"cat {naabu_out} | sort -u | tee -a {final_file}")
    naabu_out.unlink()


def run_naabu(target):
    db = connect_db()
    subs_collection = db["subdomains"]
    query = subs_collection.find({"target": target})
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for result in query:
            futures.append(executor.submit(setup_naabu, result["subdomain"]))


def naabu_parser(target):
    run_naabu(target)
    db = connect_db()
    collection = db["hostsports"]
    with open(final_file, "r") as f:
        for line in f:
            data = {
                "target": target,
                "host": line,
                "date": datetime.now(),
            }
            if collection.find_one({"host": line}):
                print(f"{data['host']} already exists id DB")
            else:
                collection.insert_one(data)
                print(f"Inserted {data['host']}")
        final_file.unlink()
