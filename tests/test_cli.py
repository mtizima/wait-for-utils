"""test_cli."""
from unittest import mock

import pytest
from click.testing import CliRunner

from wait_for_utils.cli import wait_for_postgres


@pytest.mark.parametrize(
    ("argument", "expected_exit_code"),
    [
        ("--help", 0),
        ("-v", 0),
        ("--version", 0),
        ("--test", 2),
    ],
)
def test_wait_for_postgres_info(argument, expected_exit_code):
    result = CliRunner().invoke(wait_for_postgres, [argument])
    assert result.exit_code == expected_exit_code


def test_wait_for_postgres_no_connect(monkeypatch):
    monkeypatch.setenv("POSTGRES_CHECK_TIMEOUT", "1")
    result = CliRunner().invoke(wait_for_postgres)
    assert result.exit_code == 0


@mock.patch("wait_for_utils.wait_for_pg.PGReady._connect")
def test_wait_for_postgres_mock_connect(mock_db_conn):
    result = CliRunner().invoke(wait_for_postgres)
    assert result.exit_code == 0
