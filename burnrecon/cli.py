import typer
from base import (
    getalive,
    list_subdomains,
    list_urls_from_target,
    subdomain_enum,
)

app = typer.Typer()


@app.command()
def enum(
    target: str = typer.Option(..., "--target", "-t", help="Name of target"),
    domain: str = typer.Option(..., "--domain", "-d", help="Domain of target"),
):
    """Enumerate subdomains."""
    subdomain_enum(target, domain)


@app.command()
def list_subs(
    target: str = typer.Option(..., "--target", "-t", help="Name of target")
):
    """List all subdomains of a target."""
    for subs in list_subdomains(target):
        print(subs["subdomain"])


@app.command()
def alive_hosts(
    target: str = typer.Option(..., "--target", "-t", help="Name of target")
):
    """Check if subdomain is alive."""
    getalive(target)


@app.command()
def list_urls(
    target: str = typer.Option(..., "--target", "-t", help="Name of target")
):
    """List all urls of a target."""

    urls = list_urls_from_target(target)

    for url in urls:
        print(url["url"])


if __name__ == "__main__":
    app()
