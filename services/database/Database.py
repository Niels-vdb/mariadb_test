import mariadb
import sys


class Database:
    def __init__(self) -> None:
        self.conn = None

    """
    A class used to handle connections and operations with a MariaDB database.
    """

    def connection(self, username: str, password: str) -> None:
        """
        Establishes a connection to the MariaDB database.

        Parameters:
        username (str): The username for the database connection.
        password (str): The password for the database connection.

        Raises:
        mariadb.Error: If there is an error connecting to the MariaDB platform.
        """
        try:
            self.conn = mariadb.connect(
                user=username, password=password, host="127.0.0.1", port=3306
            )
        except mariadb.Error as e:
            print(f"Error connectting to MariaDB platform: {e}")
            sys.exit(1)

    def query_executor(self, sql_query: str) -> None:
        """
        Executes a given SQL query that does not return any result (e.g., INSERT, UPDATE, DELETE).

        Parameters:
        sql_query (str): The SQL query to be executed.

        Returns:
        None
        """
        cursor = self.conn.cursor()
        cursor.execute(sql_query)
        self.conn.commit()
        cursor.close()

    def select_query(self, sql_query: str) -> object:
        """
        Executes a given SQL query and returns the result.

        Parameters:
        sql_query (str): The SQL query to be executed.

        Returns:
        object: The result of the SQL query, typically a list of tuples.
        """
        cursor = self.conn.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        cursor.close()

        return result

    def close_connection(self) -> None:
        """
        Closes the connection to the MariaDB database.

        Returns:
        None
        """
        self.conn.close()
