from database import initialize_database
from books import book_menu
from customers import customer_menu
from sales import sales_menu
from reports import reports_menu

def main():
    # Initialize the bookstore database
    initialize_database()

    # Keep showing the main menu until the user chooses to exit
    while True:
        print("\n")
        print("=" * 45)
        print("       BOOKSTORE MANAGEMENT SYSTEM")
        print("=" * 45)

        # Display the main menu options
        print("1. Book Management")
        print("2. Customer Management")
        print("3. Sales & Billing")
        print("4. Reports")
        print("5. Exit")

        # Get the user's choice
        choice = input("Enter your choice: ")

        # Open the Book Management menu
        if choice == "1":
            book_menu()

        # Open the Customer Management menu
        elif choice == "2":
            customer_menu()

        # Open the Sales and Billing menu
        elif choice == "3":
            sales_menu()

        # Open the Reports menu
        elif choice == "4":
            reports_menu()

        # Exit the program
        elif choice == "5":
            print("Thank you for using the Bookstore Management System.")
            break

        # Handle an invalid menu choice
        else:
            print("Invalid choice. Please try again.")


# Run the main function when this file is executed
if __name__ == "__main__":
    main()
