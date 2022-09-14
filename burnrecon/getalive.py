import concurrent.futures
import json
import os
import tempfile
from datetime import datetime
from pathlib import Path

from database import connect_db

random_name = tempfile.NamedTemporaryFile(delete=False)
final_file = Path(random_name.name)

httpx_tech = {}


def setup_httpx(subdomain):
    random_name = tempfile.NamedTemporaryFile(delete=False)
    httpx_out = Path(random_name.name)
    httpx_cmd = "httpx -silent -status-code -tech-detect -timeout 10 "
    httpx_cmd += f"-threads 10 -json -o {httpx_out}"
    os.system(f"echo {subdomain } | {httpx_cmd}")
    os.system(f"cat {httpx_out} >> {final_file}")
    httpx_out.unlink()


def run_httpx(target):
    db = connect_db()
    subs_collection = db["hostsports"]
    query = subs_collection.find({"target": target})
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for result in query:
            futures.append(executor.submit(setup_httpx, result["host"]))


def httpx_parser(target):
    run_httpx(target)
    db = connect_db()
    collection = db["alivehosts"]
    with open(final_file, "r") as f:
        for line in f:
            json_data = json.loads(line)
            if "technologies" in json_data:
                httpx_tech["tech"] = json_data["technologies"]
            else:
                httpx_tech["tech"] = ""

            if "webserver" in json_data:
                httpx_tech["webserver"] = json_data["webserver"]
            else:
                httpx_tech["webserver"] = ""

            if "title" in json_data:
                httpx_tech["title"] = json_data["title"]
            else:
                httpx_tech["title"] = ""

            data = {
                "target": target,
                "url": json_data["url"],
                "status-code": json_data["status-code"],
                "webserver": httpx_tech["webserver"],
                "title": httpx_tech["title"],
                "host": json_data["host"],
                "port": json_data["port"],
                "techs": httpx_tech["tech"],
                "date": datetime.now(),
            }
            if collection.find_one({"url": json_data["url"]}):
                print(f"{json_data['url']} already exists id DB")
            else:
                collection.insert_one(data)
                print(f"Inserted {json_data['url']}")
        final_file.unlink()
