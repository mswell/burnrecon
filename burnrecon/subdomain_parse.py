import os
import tempfile
from datetime import datetime
from pathlib import Path

from database import connect_db

random_name = tempfile.NamedTemporaryFile(delete=False)
final_file = Path(random_name.name)


def exec_subfinder(domain):
    subfinder_out = Path(tempfile.NamedTemporaryFile(delete=False).name)
    subfinder_cmd = f"subfinder -d {domain} -silent -o {subfinder_out}"
    os.system(subfinder_cmd)
    os.system(f"cat {subfinder_out} >> {final_file}")
    subfinder_out.unlink()


def exec_amass(domain):
    amass_out = Path(tempfile.NamedTemporaryFile(delete=False).name)
    amass_cmd = f"amass enum -passive -d {domain} -o {amass_out}"
    os.system(amass_cmd)
    os.system(f"cat {amass_out} >> {final_file}")
    amass_out.unlink()


def exec_assetfinder(domain):
    assetfinder_out = Path(tempfile.NamedTemporaryFile(delete=False).name)
    assetfinder_cmd = f"assetfinder -subs-only {domain} > {assetfinder_out}"
    os.system(assetfinder_cmd)
    os.system(f"cat {assetfinder_out} >> {final_file}")
    assetfinder_out.unlink()


def clean_results(domain):
    clean_subs = set()
    exec_subfinder(domain)
    exec_amass(domain)
    exec_assetfinder(domain)
    with open(final_file, "r") as file_:
        for line in file_:
            clean_subs.add(line.rstrip("\n"))

    return clean_subs


def run_sub_parser(target, domain, bbplatform=""):
    # TODO: config to accept a list with domains
    db = connect_db()
    collection = db["subdomains"]
    all_subs = clean_results(domain)
    for sub in all_subs:
        data = {
            "domain": domain,
            "bbplatform": bbplatform,
            "subdomain": sub,
            "target": target,
            "date": datetime.now(),
        }

        if collection.find_one({"subdomain": sub}):
            print("Document already exists")
        else:
            collection.insert_one(data)
            print(f"Inserted {sub}")

    final_file.unlink()
