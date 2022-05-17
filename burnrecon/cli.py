"""CLI interface for project_name project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
import typer
from base import getalive, list_subdomains, subdomain_enum

app = typer.Typer()


@app.command()
def enum(target: str, domain: str):
    """Enumerate subdomains."""
    subdomain_enum(target, domain)


@app.command()
def list_subs(target: str):
    """List all subdomains of a target."""
    for subs in list_subdomains(target):
        print(subs["subdomain"])


@app.command()
def alive_hosts(target: str):
    """Check if subdomain is alive."""
    getalive(target)


if __name__ == "__main__":
    app()
