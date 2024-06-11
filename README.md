# MariaDB Query Executor

This project provides a simple framework for managing and executing SQL queries on a MariaDB database. It includes two main components:

- `Database` class for handling connections and operations with the MariaDB database.
- `QueryManager` class for managing SQL query files stored in a specified directory.

## Setup
### Prerequisites

- Python 3.7+
- MariaDB server
- mariadb Python library (can be installed via pip)

### Installation

- Clone the repository to your local machine.
- Install the necessary dependencies:

```pipenv install```

## Usage
### Database Class

The Database class is used to handle connections and operations with a MariaDB database.
#### Initialization
```python
from database.Database import Database

database = Database()
```

#### Establishing a Connection

```python
database.connection("username", "password")
```

#### Executing Queries

To execute queries that do not return results (e.g., INSERT, UPDATE, DELETE):

```python
database.query_executor("YOUR_SQL_QUERY", ("ARG1", "ARG2"))
```

To execute SELECT queries and get results:
```python
result = database.select_query("YOUR_SQL_QUERY", ("ARG1", "ARG2"))
print(result)
```

#### Creating a Database
```python
database.create_database("my_new_database")
```

#### Closing the Connection
```python
database.close_connection()
```

## QueryManager Class
The `QueryManager` class is used to manage SQL query files stored in a directory.
### Initialization
```python
from database.sql import QueryManager
import os

sql_dir = os.path.join(os.path.dirname(__file__), 'database/sql_files')
qm = QueryManager(sql_dir)
```

### Retrieving SQL Queries
To retrieve the content of an SQL file:

```python
sql_query = qm.get_sql("util.switch_database.sql")
print(sql_query)
```

## Example Usage
Here's an example of how to use both the Database and QueryManager classes in main.py:
```python
from database.Database import Database
from database.sql import QueryManager
import os

sql_dir = os.path.join(os.path.dirname(__file__), 'database/sql_files')
qm = QueryManager(sql_dir)

database = Database()
database.connection("myadmin", "password")
```

#### Accessing the switch_database.sql file within the util directory
```python
switch_database = qm.get_sql("util.switch_database.sql")

# Ensure arguments are passed as tuples
database.query_executor(switch_database, ("books",))

# Close the connection
database.close_connection()
```

## Writing New SQL Queries

1. Add SQL File: Create a new .sql file in the appropriate directory under database/sql_files.
        For example, to add an insert query, you might create database/sql_files/insert/insert_new_book.sql.

2. Write SQL Query: Write your SQL query in the newly created file.
        Example content for insert_new_book.sql:        
```sql
    INSERT INTO books (title, author_id, genre_id) VALUES (%s, %s, %s);
```
3. Access the SQL Query: Use the QueryManager to access the new SQL query in your code.
```python
    insert_new_book = qm.get_sql("insert.insert_new_book.sql")
    database.query_executor(insert_new_book, ("The Winds of Winter", 1, 2))
```
## Running Tests

Tests are written using pytest. To run the tests, use the following command:

```sh
pytest tests/test_database.py
```

This will run the test cases defined in the test_database.py file and provide feedback on whether the functions in the Database class are working correctly.