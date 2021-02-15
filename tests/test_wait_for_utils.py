import psycopg2
from pytest_mock import MockerFixture

from wait_for_utils import __version__, wait_for_pg, config


def test_version():
    assert __version__ == '0.1.0'


def test_pg_ready_is_ready_can_not_connected_to_postgres(mocker: MockerFixture):
    with mocker.patch("psycopg2.connect", side_effect=psycopg2.OperationalError) as mock_connect:
        assert wait_for_pg.PGReady().is_ready(config=config.DBConfig()) is False


def test_pg_ready_is_ready_accept_connections_postgres(mocker: MockerFixture):
    with mocker.patch("psycopg2.connect"):
        assert wait_for_pg.PGReady().is_ready(config=config.DBConfig()) is True
