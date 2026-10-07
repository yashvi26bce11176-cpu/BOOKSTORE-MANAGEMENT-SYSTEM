```python
import mysql.connector


# Connect to the MySQL bookstore database
def connect_db():
    """Connect to the MySQL bookstore database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="bookstore"
    )


# Check whether the database connection can be established
def initialize_database():
    connection = connect_db()

    # Close the connection after checking it
    if connection:
        connection.close()
```
