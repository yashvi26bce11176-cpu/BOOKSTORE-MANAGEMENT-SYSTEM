from database import connect_db
from validation import validate_nonempty


def add_customer():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    customer_id = validate_nonempty(
        input("Enter Customer ID: "),
        "Customer ID"
    )

    cursor.execute(
        "SELECT customer_id FROM customers WHERE customer_id = %s",
        (customer_id,)
    )

    if cursor.fetchone():
        print("Customer ID already exists.")
        cursor.close()
        connection.close()
        return

    name = validate_nonempty(
        input("Enter Customer Name: "),
        "Customer Name"
    )

    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    query = """
        INSERT INTO customers
        (customer_id, customer_name, phone, email)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (customer_id, name, phone, email)
    )

    connection.commit()

    print("Customer added successfully.")

    cursor.close()
    connection.close()


def update_customer():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    customer_id = input("Enter Customer ID: ")

    cursor.execute(
        "SELECT * FROM customers WHERE customer_id = %s",
        (customer_id,)
    )

    if not cursor.fetchone():
        print("Customer not found.")
        cursor.close()
        connection.close()
        return

    print("\n1. Name")
    print("2. Phone")
    print("3. Email")

    choice = input("Enter choice: ")

    if choice == "1":
        field = "customer_name"
        value = input("Enter new name: ")

    elif choice == "2":
        field = "phone"
        value = input("Enter new phone: ")

    elif choice == "3":
        field = "email"
        value = input("Enter new email: ")

    else:
        print("Invalid choice.")
        cursor.close()
        connection.close()
        return

    cursor.execute(
        f"UPDATE customers SET {field} = %s WHERE customer_id = %s",
        (value, customer_id)
    )

    connection.commit()

    print("Customer updated successfully.")

    cursor.close()
    connection.close()


def delete_customer():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    customer_id = input("Enter Customer ID: ")

    cursor.execute(
        "SELECT customer_name FROM customers WHERE customer_id = %s",
        (customer_id,)
    )

    result = cursor.fetchone()

    if not result:
        print("Customer not found.")
    else:
        confirm = input(
            f"Delete customer '{result[0]}'? (y/n): "
        )

        if confirm.lower() == "y":
            cursor.execute(
                "DELETE FROM customers WHERE customer_id = %s",
                (customer_id,)
            )

            connection.commit()
            print("Customer deleted successfully.")

    cursor.close()
    connection.close()


def search_customer():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    value = input("Enter customer name or ID: ")

    query = """
        SELECT * FROM customers
        WHERE customer_id = %s
        OR customer_name LIKE %s
    """

    cursor.execute(
        query,
        (value, "%" + value + "%")
    )

    rows = cursor.fetchall()

    if not rows:
        print("No customer found.")
    else:
        print("\n" + "-" * 70)
        print(
            f"{'ID':<12}"
            f"{'Name':<25}"
            f"{'Phone':<18}"
            f"{'Email':<30}"
        )
        print("-" * 70)

        for row in rows:
            print(
                f"{row[0]:<12}"
                f"{row[1]:<25}"
                f"{row[2]:<18}"
                f"{row[3]:<30}"
            )

    cursor.close()
    connection.close()


def display_customers():
    connection = connect_db()

    if not connection:
        return

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM customers ORDER BY customer_id"
    )

    rows = cursor.fetchall()

    if not rows:
        print("No customers found.")
    else:
        for row in rows:
            print(
                f"ID: {row[0]} | "
                f"Name: {row[1]} | "
                f"Phone: {row[2]} | "
                f"Email: {row[3]}"
            )

    cursor.close()
    connection.close()


def customer_menu():
    while True:
        print("\n===== CUSTOMER MANAGEMENT =====")
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. Search Customer")
        print("5. Display Customers")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_customer()

        elif choice == "2":
            update_customer()

        elif choice == "3":
            delete_customer()

        elif choice == "4":
            search_customer()

        elif choice == "5":
            display_customers()

        elif choice == "6":
            break

        else:
            print("Invalid choice.")
