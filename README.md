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

Run with docker: **recommended 🍺**

```bash
git clone https://github.com/mswell/burnrecon.git
docker-compose up -d
```

If run without docker

## **Requirement: python 3.7 or higher**

```bash
git clone https://github.com/mswell/burnrecon.git
cd burnrecon
./install_hacktools.sh
pip3 install -r requirements.txt
```

## **Requirement: docker and docker-compose**

If you use a local instance mongodb, use docker-compose to start your local mongoDB.

```bash
docker-compose up -d mongo
```

# Settings

If you use docker-compose to run burnrecon, your settings for DB connection are in the file `docker-compose.yml`,

```yaml
version: '3.1'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    stdin_open: true
    tty: true
    depends_on:
      - mongo
    environment:
      DYNACONF_MONGO_INITDB_ROOT_USERNAME: 'root'
      DYNACONF_MONGO_INITDB_ROOT_PASSWORD: 'toor'
      DYNACONF_MONGO_DB_ADDRESS: 'mongo'
    networks:
      - backend
```

For tokens I recommended to use `.secrets.yml`.

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

To use local cli see [cli wiki](https://github.com/mswell/burnrecon/wiki/cli-usage)

To use docker see [docker wiki](https://github.com/mswell/burnrecon/wiki/Docker-usage)

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
