"""run."""
import click

from wait_for_utils import wait_for_pg, config, __version__


@click.command()
@click.help_option("-h", "--help")
@click.version_option(
    __version__,
    "-v",
    "--version",
    message="Version of wait_for_utils %(version)s"
)
@click.option(
    "-p",
    "--port",
    type=int,
    help="Port"
)
@click.option(
    "-d",
    "--database",
    type=str,
    help="Database name"
)
@click.option(
    "-u",
    "--username",
    type=str,
    help="Username"
)
@click.password_option(help="Password")
@click.option(
    "-h",
    "--host",
    type=str,
    help="Host"
)
@click.option(
    "-t",
    "--timeout",
    metavar="seconds",
    type=int,
    help="Check timeout"
)
@click.option(
    "-i",
    "--interval",
    metavar="seconds",
    type=str,
    help="Check interval"
)
@click.argument("commands", nargs=-1)
def wait_for_postgres(**kwargs):
    """Wait for service to be available.

    :return:
    """
    wait_for_pg.PGReady().is_ready(config=config.DBConfig())


if __name__ == "__main__":
    wait_for_postgres()
