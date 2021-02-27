from unittest import mock

import psycopg2

from wait_for_utils import __version__, config, wait_for_pg


def test_version():
    assert __version__ == "0.1.0-alpha.9"


@mock.patch("psycopg2.connect")
def test_pg_ready_is_ready_accept_connections_postgres(mock_connect):
    assert wait_for_pg.PGReady().is_ready(config=config.DBConfig()) is True


@mock.patch("psycopg2.connect", side_effect=psycopg2.OperationalError())
def test_pg_ready_is_ready_can_not_connected_to_postgres(mock_connect):
    assert wait_for_pg.PGReady().is_ready(config=config.DBConfig()) is False
