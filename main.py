from database.Database import Database
from database.QueryManager import QueryManager
import os

sql_dir = os.path.join(os.path.dirname(__file__), 'database/sql_files')
qm = QueryManager(sql_dir)

database = Database()
database.connection("myadmin", "password")

# Accessing the switch_database.sql file within the util directory
switch_database = qm.get_sql("util.switch_database.sql")
insert_book = qm.get_sql("insert.insert_book.sql")
delete_book = qm.get_sql("delete.delete_book.sql")
create_database = qm.get_sql("util.create_database.sql")

print(switch_database)

# Ensure arguments are passed as tuples
database.query_executor(switch_database, ("test_db",))
database.query_executor(insert_book, ("A Game of Thrones", 3, 3))
# database.query_executor(delete_book, ("A Game of Thrones",))
database.query_executor(create_database, ("prod_db",))
