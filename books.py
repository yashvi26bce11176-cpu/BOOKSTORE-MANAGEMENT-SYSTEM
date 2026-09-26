from database import connect_db
from validation import validate_nonempty, validate_int, validate_float


def add_book():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    book_id = validate_nonempty(input("Enter Book ID: "), "Book ID")

    cursor.execute(
        "SELECT book_id FROM books WHERE book_id = %s",
        (book_id,)
    )

    if cursor.fetchone():
        print("Book ID already exists.")
        cursor.close()
        connection.close()
        return

    book_name = validate_nonempty(
        input("Enter Book Name: "), "Book Name"
    )

    author = validate_nonempty(
        input("Enter Author: "), "Author"
    )

    publisher = input("Enter Publisher: ")

    price = validate_float(
        input("Enter Price: "), "Price"
    )

    category = input("Enter Category: ")

    quantity = validate_int(
        input("Enter Quantity: "), "Quantity"
    )

    query = """
        INSERT INTO books
        (book_id, book_name, author, publisher, price, category, quantity)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        book_id,
        book_name,
        author,
        publisher,
        price,
        category,
        quantity
    )

    cursor.execute(query, values)
    connection.commit()

    print("Book added successfully.")

    cursor.close()
    connection.close()


def update_book():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    book_id = input("Enter Book ID to update: ")

    cursor.execute(
        "SELECT * FROM books WHERE book_id = %s",
        (book_id,)
    )

    if not cursor.fetchone():
        print("Book not found.")
        cursor.close()
        connection.close()
        return

    print("\nWhat do you want to update?")
    print("1. Book Name")
    print("2. Author")
    print("3. Publisher")
    print("4. Price")
    print("5. Category")
    print("6. Quantity")

    choice = input("Enter choice: ")

    fields = {
        "1": ("book_name", "Book Name"),
        "2": ("author", "Author"),
        "3": ("publisher", "Publisher"),
        "4": ("price", "Price"),
        "5": ("category", "Category"),
        "6": ("quantity", "Quantity")
    }

    if choice not in fields:
        print("Invalid choice.")
        cursor.close()
        connection.close()
        return

    field, field_name = fields[choice]

    if choice == "4":
        value = validate_float(
            input("Enter new price: "), "Price"
        )

    elif choice == "6":
        value = validate_int(
            input("Enter new quantity: "), "Quantity"
        )

    else:
        value = validate_nonempty(
            input("Enter new value: "), field_name
        )

    query = f"UPDATE books SET {field} = %s WHERE book_id = %s"

    cursor.execute(query, (value, book_id))
    connection.commit()

    print("Book updated successfully.")

    cursor.close()
    connection.close()


def delete_book():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    book_id = input("Enter Book ID to delete: ")

    cursor.execute(
        "SELECT book_name FROM books WHERE book_id = %s",
        (book_id,)
    )

    result = cursor.fetchone()

    if not result:
        print("Book not found.")
        cursor.close()
        connection.close()
        return

    confirm = input(
        f"Delete '{result[0]}'? (y/n): "
    )

    if confirm.lower() == "y":

       try:
           cursor.execute(
               "DELETE FROM books WHERE book_id = %s",
               (book_id,)
           )

           connection.commit()
           print("Book deleted successfully.")

       except Exception:
           connection.rollback()
           print("Cannot delete this book because it has existing sales records.")

    else:
        print("Deletion cancelled.")

    cursor.close()
    connection.close()


def search_books():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    print("\nSEARCH BOOKS")
    print("1. Book ID")
    print("2. Book Name")
    print("3. Author")
    print("4. Category")

    choice = input("Enter choice: ")

    if choice == "1":
        value = input("Enter Book ID: ")

        query = """
            SELECT book_id, book_name, author, publisher,
               price, category, quantity
        FROM books
        WHERE book_id = %s
        """

        cursor.execute(query, (value,))

    elif choice == "2":
        value = input("Enter Book Name: ")

        query = """
            SELECT book_id, book_name, author, publisher,
               price, category, quantity
        FROM books
        WHERE book_name LIKE %s
        """

        cursor.execute(query, ("%" + value + "%",))

    elif choice == "3":
        value = input("Enter Author: ")

        query = """
            SELECT book_id, book_name, author, publisher,
               price, category, quantity
        FROM books
        WHERE author LIKE %s
        """

        cursor.execute(query, ("%" + value + "%",))

    elif choice == "4":
        value = input("Enter Category: ")

        query = """
            SELECT book_id, book_name, author, publisher,
               price, category, quantity
        FROM books
        WHERE category LIKE %s
        """

        cursor.execute(query, ("%" + value + "%",))

    else:
        print("Invalid choice.")
        cursor.close()
        connection.close()
        return

    rows = cursor.fetchall()

    if not rows:
        print("No books found.")
    else:
        display_rows(rows)

    cursor.close()
    connection.close()


def display_rows(rows):
    print("\n" + "-" * 100)
    print(
        f"{'ID':<10}"
        f"{'Book Name':<25}"
        f"{'Author':<20}"
        f"{'Price':<10}"
        f"{'Category':<15}"
        f"{'Qty':<8}"
    )
    print("-" * 100)

    for row in rows:
        print(
            f"{row[0]:<10}"
            f"{row[1][:23]:<25}"
            f"{row[2][:18]:<20}"
            f"{float(row[4]):<10.2f}"
            f"{str(row[5])[:13]:<15}"
            f"{row[6]:<8}"
        )

    print("-" * 100)


def display_all_books():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    cursor.execute("""
    SELECT book_id, book_name, author, publisher,
           price, category, quantity
    FROM books
    ORDER BY book_id
""")

    rows = cursor.fetchall()

    if not rows:
        print("No books available.")
    else:
        display_rows(rows)

    cursor.close()
    connection.close()


def book_menu():
    while True:
        print("\n===== BOOK MANAGEMENT =====")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Search Book")
        print("5. Display All Books")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            update_book()

        elif choice == "3":
            delete_book()

        elif choice == "4":
            search_books()

        elif choice == "5":
            display_all_books()

        elif choice == "6":
            break

        else:
            print("Invalid choice.")
