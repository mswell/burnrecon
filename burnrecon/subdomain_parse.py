import tempfile
import os
import requests
from pathlib import Path
from datetime import datetime


random_name = tempfile.NamedTemporaryFile(delete=False)
final_file = Path(random_name.name)


def exec_subfinder(domain):
    subfinder_out = Path(tempfile.NamedTemporaryFile(delete=False).name)
    subfinder_cmd = f"subfinder -d {domain} -silent -o {subfinder_out}"
    os.system(subfinder_cmd)
    os.system(f"cat {subfinder_out} >> {final_file}")
    subfinder_out.unlink()


# TODO: add findomain

# TODO: add amass
def exec_crtsh(domain):
    r = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")
    result = set()
    for subdomain in r.json():
        sub_strings = subdomain["common_name"].lstrip("*.")
        result.add(sub_strings)

    return result


def clean_results(domain):
    clean_subs = set()
    exec_subfinder(domain)
    with open(final_file, "r") as f:
        for line in f:
            clean_subs.add(line.rstrip("\n"))

        for subs in exec_crtsh(domain):
            clean_subs.add(subs)

    return clean_subs


def run_sub_parser(target, domain):
    all_subs = clean_results(domain)
    for sub in all_subs:
        data = {
            "domain": domain,
            "subdomain": sub,
            "target": target,
            "date": datetime.now(),
        }
        print(data)


# exec_subfinder(domain)

# allsubdomains = set()
# with open(final_file, "r") as f:
#     for line in f:
#         allsubdomains.add(line.rstrip("\n"))


# for sub in allsubdomains:
#     print(sub)
