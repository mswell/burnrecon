import tempfile
import os
import sys
import requests
from pprint import pprint
from pathlib import Path


domain = sys.argv[1]

random_name = tempfile.NamedTemporaryFile(delete=False)
final_file = Path(random_name.name)

# TODO: add subfinder
def exec_subfinder(domain):
    subfinder_out = Path(tempfile.NamedTemporaryFile(delete=False).name)
    subfinder_cmd = f"subfinder -d {domain} -silent -o {subfinder_out}"
    os.system(subfinder_cmd)
    os.system(f"cat {subfinder_out} >> {final_file}")
    subfinder_out.unlink()


# TODO: add findomain

# TODO: add crt.sh


def exec_crtsh(domain):
    r = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")
    result = set()
    for subdomain in r.json():
        sub_strings = subdomain["common_name"].lstrip("*.")
        result.add(sub_strings)

    for subs in result:
        os.system(f"echo {subs} >> {final_file}")


exec_crtsh(domain)

exec_subfinder(domain)

allsubdomains = set()
with open(final_file, "r") as f:
    for line in f:
        allsubdomains.add(line.rstrip("\n"))


for sub in allsubdomains:
    print(sub)
