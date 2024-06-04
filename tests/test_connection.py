import pytest
import sys
import pathlib
import mariadb

root_dir = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(root_dir)

my_path = sys.path

from connection import connection

def test_create_connection():
    username = 'myadmin'
    password = 'password'
    ip_address = '127.0.0.1'
    database_name = 'test_db'

    conn = connection(username, password, ip_address, database_name)

    assert conn == True

def test_create_connection_invalid():
    username = 'falseadmin'
    password = 'password'
    ip_address = '127.0.0.1'
    database_name = 'test_db'

    with pytest.raises(SystemExit):
        conn = connection(username, password, ip_address, database_name)
