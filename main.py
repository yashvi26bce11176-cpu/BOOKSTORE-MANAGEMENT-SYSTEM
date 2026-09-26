from database import initialize_database
from books import book_menu
from customers import customer_menu
from sales import sales_menu
from reports import reports_menu

def main():
    initialize_database()

    while True:
        print("\n")
        print("=" * 45)
        print("       BOOKSTORE MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Book Management")
        print("2. Customer Management")
        print("3. Sales & Billing")
        print("4. Reports")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_menu()

        elif choice == "2":
            customer_menu()

        elif choice == "3":
            sales_menu()

        elif choice == "4":
            reports_menu()

        elif choice == "5":
            print("Thank you for using the Bookstore Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
