from database import connect_db


def make_sale():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    customer_id = input("Enter Customer ID: ")

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

    book_id = input("Enter Book ID: ")

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

    print("\nBook:", book_name)
    print("Price:", float(price))
    print("Available stock:", stock)

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

    if quantity > stock:
        print("Insufficient stock.")
        cursor.close()
        connection.close()
        return

    total = float(price) * quantity

    cursor.execute(
        """
        INSERT INTO sales
        (customer_id, book_id, quantity, total_amount)
        VALUES (%s, %s, %s, %s)
        """,
        (customer_id, book_id, quantity, total)
    )

    cursor.execute(
        """
        UPDATE books
        SET quantity = quantity - %s
        WHERE book_id = %s
        """,
        (quantity, book_id)
    )

    connection.commit()

    sale_id = cursor.lastrowid

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


def view_sales():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

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
        LEFT JOIN books b
            ON s.book_id = b.book_id
        ORDER BY s.sale_date DESC
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    if not rows:
        print("No sales recorded.")

    else:
        print("\n" + "-" * 100)
        print(
            f"{'Sale ID':<10}"
            f"{'Customer':<20}"
            f"{'Book':<25}"
            f"{'Qty':<8}"
            f"{'Total':<12}"
            f"{'Date':<20}"
        )
        print("-" * 100)

        for row in rows:
            print(
                f"{row[0]:<10}"
                f"{str(row[1])[:18]:<20}"
                f"{str(row[2])[:23]:<25}"
                f"{row[3]:<8}"
                f"{float(row[4]):<12.2f}"
                f"{str(row[5]):<20}"
            )

    cursor.close()
    connection.close()


def sales_menu():
    while True:
        print("\n===== SALES & BILLING =====")
        print("1. Make Sale")
        print("2. View Sales History")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            make_sale()

        elif choice == "2":
            view_sales()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")
