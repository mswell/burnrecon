from subdomain_parse import run_sub_parser
from database import connect_db


def subdomain_enum(target, domain):
    run_sub_parser(target, domain)


def list_subdomains(target):
    db = connect_db()
    collection = db["subdomains"]
    query = collection.find({"target": target})
    return query
