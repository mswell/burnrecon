import sys

import validators
from database import connect_db
from getalive import httpx_parser
from subdomain_parse import run_sub_parser


def subdomain_enum(target, domain):
    valid_domain = validators.domain(domain)
    if valid_domain:
        run_sub_parser(target, domain)
    else:
        raise NameError(
            sys.exit(f"{domain} is not a valid domain patterns, ex: example.com")
        )


def list_subdomains(target):
    db = connect_db()
    collection = db["subdomains"]
    query = collection.find({"target": target})
    return query


def getalive(target):
    httpx_parser(target)
