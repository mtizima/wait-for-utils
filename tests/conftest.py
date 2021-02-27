"""conftest."""
import psycopg2
import pytest


@pytest.fixture()
def db_conn():
    dbc = psycopg2.connect()
    return dbc


@pytest.fixture()
def mock_db_conn(mocker, db_conn):
    mocker.patch('db.database.dbc', db_conn)
    return True
