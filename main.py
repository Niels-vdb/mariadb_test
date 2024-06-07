from services.database.Database import Database

database = Database()

book_list = []

conn = database.connection("myadmin", "password")

database.query_executor("USE test_db;")

database.query_executor(
    """INSERT INTO books (Title,SeriesID,AuthorID) 
VALUES('A Game of Thrones',3,3); """
)

books = database.select_query("SELECT * FROM books;")
for bookID, Title, SeriesID, AuthorID in books:
    book_list.append(f"{bookID}: {Title}")
print(book_list)

book_list.clear()

database.query_executor("DELETE FROM books WHERE Title = 'A Game of Thrones';")

books = database.select_query("SELECT * FROM books;")
for bookID, Title, SeriesID, AuthorID in books:
    book_list.append(f"{bookID}: {Title}")
print(book_list)


database.close_connection()
