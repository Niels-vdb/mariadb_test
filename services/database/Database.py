import mariadb
import sys


class Database:
    def connection(self, username: str, password: str):
        try:
            self.conn = mariadb.connect(
                user=username, password=password, host="127.0.0.1", port=3306
            )
        except mariadb.Error as e:
            print(f"Error connectting to MariaDB platform: {e}")
            sys.exit(1)

    def query_executor(self, sql_query: str):
        cursor = self.conn.cursor()
        cursor.execute(sql_query)
        self.conn.commit()
        cursor.close()

    def select_query(self, sql_query: str):
        cursor = self.conn.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        cursor.close()

        return result

    def close_connection(self):
        self.conn.close()
