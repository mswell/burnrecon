from database import connect_db
from getalive import httpx_parser
from subdomain_parse import run_sub_parser


def subdomain_enum(target, domain):
    run_sub_parser(target, domain)


def list_subdomains(target):
    db = connect_db()
    collection = db["subdomains"]
    query = collection.find({"target": target})
    return query


def getalive(target):
    httpx_parser(target)
