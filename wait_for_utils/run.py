"""run."""
from wait_for_utils import wait_for_pg, config


def cli():
    """Process command lines arguments.

    :return:
    """
    wait_for_pg.PGReady().is_ready(config=config.DBConfig())
