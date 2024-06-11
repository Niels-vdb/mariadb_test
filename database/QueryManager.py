import os
from typing import Dict

class QueryManager:
    """
    A class to manage SQL query files stored in a directory.

    Attributes:
    sql_dir (str): The directory where SQL files are stored.
    sql_files (dict): A dictionary mapping file keys to their file paths.
    """
    sql_dir = None
    sql_files = None

    def __init__(self, sql_dir: str) -> None:
        """
        Initializes the QueryManager with the given directory containing SQL files.

        Parameters:
        sql_dir (str): The directory where SQL files are stored.
        """
        self.sql_dir = sql_dir
        self.sql_files = self._find_sql_files()
        
    def _find_sql_files(self) -> Dict[str, str]:  
        """
        Finds all SQL files in the specified directory and maps them to their file paths.

        Returns:
        dict: A dictionary where keys are relative paths (with dots as separators) and values are absolute file paths.
        """  
        sql_files = {}
        for root, _, files in os.walk(self.sql_dir):
            for file in files:
                if file.endswith('.sql'):
                    file_path = os.path.join(root, file)
                    file_key = os.path.relpath(file_path, self.sql_dir).replace(os.sep, '.')
                    sql_files[file_key] = file_path

        return sql_files

    def get_sql(self, key: str) -> str:
        """
        Retrieves the SQL query content from a file specified by the given key.

        Parameters:
        key (str): The key representing the relative path to the SQL file (with dots as separators).

        Returns:
        str: The SQL query content.

        Raises:
        AttributeError: If the specified key does not exist in the sql_files dictionary.
        """
        if key in self.sql_files:
            with open(self.sql_files[key], "r") as file:
                return file.read()
        else:
            raise AttributeError(f"QueryManager cannot find file '{key}'")
