```python
from database import connect_db
from validation import validate_nonempty, validate_int, validate_float


# Add a new book to the bookstore
def add_book():
    # Connect to the database
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    # Get and validate the Book ID
    book_id = validate_nonempty(input("Enter Book ID: "), "Book ID")

    # Check whether the Book ID already exists
    cursor.execute(
        "SELECT book_id FROM books WHERE book_id = %s",
        (book_id,)
    )

    if cursor.fetchone():
        print("Book ID already exists.")
        cursor.close()
        connection.close()
        return

    # Get book details from the user
    book_name = validate_nonempty(
        input("Enter Book Name: "), "Book N
```
