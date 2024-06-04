import mariadb
import sys

# Connect to MariaDB
def connection(username:str, password:str, ip_address:str, database_name:str):
    try:
        conn = mariadb.connect(
            user = username,
            password = password,
            host = ip_address,
            port = 3306,
            database = database_name   
        )
    except mariadb.Error as e:
        print(f"Error connectting to MariaDB platform: {e}")
        sys.exit(1)

    # Get cursor
    if conn.cursor():
        return True
    else:
        return False 

# conn = connection()

# print(conn)