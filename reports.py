```python
from database import connect_db


# Generate a report showing the current inventory
def inventory_report():
    # Connect to the database
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    # Calculate total book titles, total quantity and inventory value
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


# Generate a report of books with low stock
def low_stock_report():
    # Connect to the database
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    # Find books having 3 or fewer copies available
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
        # Display each low-stock book
        for row in rows:
            print(
                f"ID: {row[0]} | "
                f"Book: {row[1]} | "
                f"Remaining: {row[2]}"
            )

    cursor.close()
    connection.close()


# Generate a report showing overall sales information
def sales_report():
    # Connect to the database
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    # Calculate total transactions, books sold and revenue
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


# Display books according to the number of copies sold
def best_selling_books():
    # Connect to the database
    connection
```
