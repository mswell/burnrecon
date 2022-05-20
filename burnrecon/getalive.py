import tempfile
import json
import concurrent.futures
from database import connect_db
from pathlib import Path
from datetime import datetime
import subprocess

random_name = tempfile.NamedTemporaryFile(delete=False)
subdomains_file = Path(random_name.name)
httpx_tech = {}
httpx_response = ""


def setup_httpx():
    global httpx_response
    httpx_cmd = f"httpx -silent -status-code -tech-detect -timeout 10 "
    httpx_cmd += f"-threads 10 -json -silent"
    httpx_response = subprocess.check_output(
        f"cat {subdomains_file} | {httpx_cmd}", shell=True).decode("utf-8") 
    subdomains_file.unlink()


def run_httpx(target):
    db = connect_db()
    subs_collection = db["subdomains"]
    query = subs_collection.find({"target": target})
    subdomains = [result["subdomain"] for result in query]
    with open(subdomains_file, "w") as file_subdomains:
        file_subdomains.write("\n".join(subdomains))

    setup_httpx()

def httpx_parser(target):
    run_httpx(target)
    db = connect_db()
    collection = db["alivehosts"]
    data_list = []
    for line in httpx_response.split("\n"):
        if(line == ""): continue
        json_data = json.loads(line)
        if "technologies" in json_data:
            httpx_tech["tech"] = json_data["technologies"]
        else:
            httpx_tech["tech"] = ""

        if "webserver" in json_data:
            httpx_tech["webserver"] = json_data["webserver"]
        else:
            httpx_tech["webserver"] = ""

        data = {
                "target": target,
                "url": json_data["url"],
                "status-code": json_data["status-code"],
                "webserver": httpx_tech["webserver"],
                "host": json_data["host"],
                "port": json_data["port"],
                "techs": httpx_tech["tech"],
                "date": datetime.now(),
            }
        if collection.find_one({"url": json_data["url"]}):
            print(f"{json_data['url']} already exists id DB")
        else:
            data_list.append(data)
            print(f"Inserted {json_data['url']}")
    if (len(data_list) > 0):
        collection.insert_many(data_list)
