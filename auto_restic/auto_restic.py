# -*- coding: utf-8 -*-

"""Main Auto Restic script"""
import sys
import os
import click
import subprocess


@click.command()
def main(args=None):
    """Console script for auto_restic."""
    try:
        result = subprocess.run(["restic", "list"], stdout=subprocess.PIPE)
        print(result.stdout)
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            click.secho("ERROR: Restic not installed.", fg="red", bold=True)
        else:
            click.secho("ERROR: Some other error.", fg="red", bold=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
