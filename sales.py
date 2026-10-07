```python
from database import connect_db


# Make a new sale and generate the bill
def make_sale():
    """Record a new sale and generate the bill."""
    # Connect to the database
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    # Get the Customer ID
    customer_id = input("Enter Customer ID: ")

    # Check whether the customer exists
    cursor.execute(
        "SELECT customer_name FROM customers WHERE customer_id = %s",
        (customer_id,)
    )

    customer = cursor.fetchone()

    if not customer:
        print("Customer not found.")
        cursor.close()
        connection.close()
        return

    # Get the Book ID
    book_id = input("Enter Book ID: ")

    # Find the book details and available stock
    cursor.execute(
        """
        SELECT book_name, price, quantity
        FROM books
        WHERE book_id = %s
        """,
        (book_id,)
    )

    book = cursor.fetchone()

    if not book:
        print("Book not found.")
        cursor.close()
        connection.close()
        return

    book_name, price, stock = book

    # Display the selected book details
    print("\nBook:", book_name)
    print("Price:", float(price))
    print("Available stock:", stock)

    # Get and validate the quantity to be sold
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            cursor.close()
            connection.close()
            return

    except ValueError:
        print("Invalid quantity.")
        cursor.close()
        connection.close()
        return

    # Check whether enough books are available
    if quantity > stock:
        print("Insufficient stock.")
        cursor.close()
        connection.close()
        return

    # Calculate the total amount of the sale
    total = float(price) * quantity

    # Store the sale details in the sales table
    cursor.execute(
        """
        INSERT INTO sales
        (customer_id, book_id, quantity, total_amount)
        VALUES (%s, %s, %s, %s)
        """,
        (customer_id, book_id, quantity, total)
    )

    # Reduce the book quantity after the sale
    cursor.execute(
        """
        UPDATE books
        SET quantity = quantity - %s
        WHERE book_id = %s
        """,
        (quantity, book_id)
    )

    # Save the changes to the database
    connection.commit()

    # Get the ID of the newly created sale
    sale_id = cursor.lastrowid

    # Display the bill
    print("\n========== BILL ==========")
    print("Sale ID:", sale_id)
    print("Customer:", customer[0])
    print("Book:", book_name)
    print("Quantity:", quantity)
    print("Price per book:", float(price))
    print("Total Amount:", total)
    print("==========================")

    cursor.close()
    connection.close()


# Display the history of all sales
def view_sales():
    # Connect to the database
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    # Retrieve sales along with customer and book details
    query = """
        SELECT
            s.sale_id,
            c.customer_name,
            b.book_name,
            s.quantity,
            s.total_amount,
            s.sale_date
        FROM sales s
        LEFT JOIN customers c
            ON s.customer_id = c.customer_id
```
