from database import connect_db


def inventory_report():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            COALESCE(SUM(quantity), 0),
            COALESCE(SUM(price * quantity), 0)
        FROM books
    """)

    total_books, total_quantity, stock_value = cursor.fetchone()

    print("\n===== INVENTORY REPORT =====")
    print("Different book titles:", total_books)
    print("Total books in stock:", total_quantity)
    print("Total inventory value:", float(stock_value))

    cursor.close()
    connection.close()


def low_stock_report():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    cursor.execute("""
        SELECT book_id, book_name, quantity
        FROM books
        WHERE quantity <= 3
        ORDER BY quantity
    """)

    rows = cursor.fetchall()

    print("\n===== LOW STOCK REPORT =====")

    if not rows:
        print("No books are currently low in stock.")

    else:
        for row in rows:
            print(
                f"ID: {row[0]} | "
                f"Book: {row[1]} | "
                f"Remaining: {row[2]}"
            )

    cursor.close()
    connection.close()


def sales_report():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            COALESCE(SUM(quantity), 0),
            COALESCE(SUM(total_amount), 0)
        FROM sales
    """)

    transactions, books_sold, revenue = cursor.fetchone()

    print("\n===== SALES REPORT =====")
    print("Total transactions:", transactions)
    print("Total books sold:", books_sold)
    print("Total revenue:", float(revenue))

    cursor.close()
    connection.close()


def best_selling_books():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            b.book_name,
            SUM(s.quantity) AS total_sold
        FROM sales s
        JOIN books b
            ON s.book_id = b.book_id
        GROUP BY b.book_id, b.book_name
        ORDER BY total_sold DESC
    """)

    rows = cursor.fetchall()

    print("\n===== BEST SELLING BOOKS =====")

    if not rows:
        print("No sales available.")

    else:
        for index, row in enumerate(rows, start=1):
            print(
                f"{index}. {row[0]} - "
                f"{row[1]} copies sold"
            )

    cursor.close()
    connection.close()


def reports_menu():
    while True:
        print("\n===== REPORTS =====")
        print("1. Inventory Report")
        print("2. Low Stock Report")
        print("3. Sales Report")
        print("4. Best Selling Books")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            inventory_report()

        elif choice == "2":
            low_stock_report()

        elif choice == "3":
            sales_report()

        elif choice == "4":
            best_selling_books()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")
