import pytest
import sys
import pathlib

root_dir = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(root_dir)

my_path = sys.path

from database.Database import Database

database = Database()

def test_create_connection():
    username = 'myadmin'
    password = 'password'

    conn = database.connection(username, password)

    assert conn == None

def test_create_connection_invalid():
    username = 'falseadmin'
    password = 'password'

    with pytest.raises(SystemExit):
        database.connection(username, password)
