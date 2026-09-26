import mysql.connector


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="bookstore"
    )


def initialize_database():
    connection = connect_db()

    if connection:
        connection.close()
