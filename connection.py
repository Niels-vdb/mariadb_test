import mariadb
import sys

# Connect to MAriaDB
try:
    conn = mariadb.connect(
        user="myadmin",
        password='password',
        host='127.0.0.1',
        port=3306,
        database='test_db'   
    )
except mariadb.Error as e:
    print(f"Error connectting to MariaDB platform: {e}")
    sys.exit(1)

# Get cursor
cur = conn.cursor()

print(cur)