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

    def query_executor(self, sql_query: str, args: tuple) -> None:
        """
        Executes a given SQL query that does not return any result (e.g., INSERT, UPDATE, DELETE).

        Parameters:
        sql_query (str): The SQL query to be executed.
        args (tuple): The arguments given to the query.

        Returns:
        None
        """
        cursor = self.conn.cursor()
        print(f"query: {sql_query}")
        print(f"args: {args}")
        if "USE" in sql_query or "CREATE DATABASE" in sql_query:
            formatted_query = sql_query % args
            cursor.execute(formatted_query)
        else:
            cursor.execute(sql_query, args)
            self.conn.commit()
        cursor.close()

    def select_query(self, sql_query: str, args: tuple) -> object:
        """
        Executes a given SQL query and returns the result.

        Parameters:
        sql_query (str): The SQL query to be executed.
        args (tuple): The arguments given to the query.

        Returns:
        object: The result of the SQL query, typically a list of tuples.
        """
        cursor = self.conn.cursor()
        cursor.execute(sql_query, args)
        result = cursor.fetchall()
        cursor.close()

        return result

    def create_database(self, db_name: str = None) -> None:
        """
        Alowes creation of a new database.

        Parameters:
        db_name (str) optional: The name of the new database.
        If none is given user will be promted in stdout.

        Returns:
        None

        Raises:
        mariadb.Error: If there is an error creating the database.
        """
        if db_name == None:
            db_name = input("Name your new database: ")

        query = "CREATE DATABASE %(db_name)s;"
        args = {"db_name": db_name}

        try:
            self.query_executor(query, args)
        except mariadb.Error as e:
            print(f"Database could not be created see following error: {e}")

    def close_connection(self) -> None:
        """
        Closes the connection to the MariaDB database.

        Returns:
        None
        """
        self.conn.close()
