"""CLI interface for project_name project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
import sys
from base import subdomain_enum


target = sys.argv[1]
domain = sys.argv[2]
subdomain_enum(target, domain)


def main():

    # pragma: no cover
    """
    The main function executes on commands:
    `python -m project_name` and `$ project_name `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
