"""CLI interface for project_name project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
import typer
from base import subdomain_enum, list_subdomains

app = typer.Typer()


@app.command()
def enum(target: str, domain: str):
    subdomain_enum(target, domain)


@app.command()
def list_subs(target: str):
    for subs in list_subdomains(target):
        print(subs["subdomain"])


if __name__ == "__main__":
    app()
