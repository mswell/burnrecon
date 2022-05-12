import tempfile
import os
import sys
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

exec_subfinder(domain)
with open(final_file, "r") as f:
    for line in f:
        print(line.rstrip("\n"))
