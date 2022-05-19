<!-- markdownlint-disable -->
<h1 align="center">
    BurnRecon
</h1>
<!-- markdownlint-restore -->

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

----

# Description

**BurnRecon** is a tool to automate and organize reconnaissance operations.

Built with ❤️ and:

- [Python](https://www.python.org/)
- [Mongodb](https://www.mongodb.com/pt-br)
- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/install/)

----

# Instalation

### **Requirement: python 3.7 or higher**

```bash
git clone https://github.com/mswell/burnrecon.git
cd burnrecon
./install_hacktools.sh
pip3 install -r requirements.txt
```

### **Requirement: docker and docker-compose**

If you use a local instance mongodb, use docker-compose to start your local mongoDB.

```bash
cd burnrecon/docker
docker-compose up -d
```

# Settings

You need to set your config in [settings](burnrecon/settings.toml) file.

```toml
[database]
address = 'localhost'
```

You need to set your secrets in the [secrets](burnrecon/.secrets_example.toml) file.

```toml
MONGO_DB_USER = 'root'
MONGO_DB_PASS = 'toor'
DISCORD_TOKEN = ''
```

## **Please remember to mv .secrets_example.toml to .secrets.toml**

----

# Usage

to use cli run:

```bash
cd burnrecon/burnrecon

python3 cli.py --help
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  alive-hosts  Check if subdomain is alive.
  enum         Enumerate subdomains.
  list-subs    List all subdomains of a target.
  list-urls    List all urls of a target.


```

Enum subdomains:

```bash
python3 cli.py enum -t hackerone -d hackerone.com

python3 cli.py enum --help
Usage: cli.py enum [OPTIONS]

  Enumerate subdomains.

Options:
  -t, --target TEXT  Name of target  [required]
  -d, --domain TEXT  Domain of target  [required]
  --help             Show this message and exit.
```

List subdomains:

```bash
python3 cli.py list-subs -t hackerone

python3 cli.py list-subs --help
Usage: cli.py list-subs [OPTIONS]

  List all subdomains of a target.

Options:
  -t, --target TEXT  Name of target  [required]
  --help             Show this message and exit.
```

Test alive hosts:

```bash
python3 cli.py alive-hosts -t hackerone

python3 cli.py alive-hosts --help
Usage: cli.py alive-hosts [OPTIONS]

  Check if subdomain is alive.

Options:
  -t, --target TEXT  Name of target  [required]
  --help             Show this message and exit.
```

List alive urls:

```bash

python3 cli.py list-urls -t hackerone

python3 cli.py list-urls --help
Usage: cli.py list-urls [OPTIONS]

  List all urls of a target.

Options:
  -t, --target TEXT  Name of target  [required]
  --help             Show this message and exit.

```

----

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
