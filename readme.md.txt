# Bookstore Management System

## 1. Project Title

Bookstore Management System

## 2. Project Description

The Bookstore Management System is a menu-driven Python application developed to manage the daily operations of a bookstore.

The system allows the user to manage books and customers, process sales, automatically update stock, and generate useful reports.

The project uses Python for the application logic and MySQL for storing and managing data.

## 3. Objectives

The main objectives of this project are:

- To maintain book records efficiently.
- To manage customer information.
- To process bookstore sales and generate bills.
- To automatically reduce book stock after a sale.
- To search and update records easily.
- To generate inventory and sales reports.
- To demonstrate the use of Python with a MySQL database.

## 4. Major Functional Modules

### 4.1 Book Management

This module allows the user to:

- Add new books.
- Update existing book information.
- Delete books.
- Search for books using different criteria.
- Display all available books.

### 4.2 Customer Management

This module allows the user to:

- Add customers.
- Update customer information.
- Delete customers.
- Search for customers.
- Display customer records.

### 4.3 Sales and Billing

This module allows the user to:

- Select a customer.
- Select a book.
- Enter the required quantity.
- Calculate the total amount.
- Generate a bill.
- Automatically reduce the available stock.
- View sales history.

### 4.4 Reports

This module generates:

- Inventory reports.
- Low-stock reports.
- Sales reports.
- Best-selling book reports.

## 5. Technologies Used

- Python
- MySQL
- mysql-connector-python
- MySQL Shell
- Python IDLE

## 6. Project Structure

Bookstore-Management-System
│
├── main.py
├── books.py
├── customers.py
├── sales.py
├── reports.py
├── validation.py
├── database.py
├── database.sql
├── README.md
└── Project Documentation.docx

## 7. Description of Python Files
main.py:

->Contains the main menu and controls the overall flow of the application.

books.py:

->Contains functions related to book management such as adding, updating, deleting, searching, and displaying books.

customers.py:

->Contains functions for adding, updating, deleting, searching, and displaying customer records.

sales.py:

->Handles sales transactions, billing, stock reduction, and sales history.

reports.py:

->Generates inventory, low-stock, sales, and best-selling book reports.

validation.py:

->Contains input validation functions used throughout the project.

database.py:

->Contains the function used to establish a connection between Python and MySQL.

database.sql:

->Contains the SQL commands required to create the bookstore database and its tables.

## 8. Database Design

The system contains three main tables:

Books:

->Stores information about books available in the bookstore.

Customers:

->Stores information about bookstore customers.

Sales:

->Stores information about completed sales transactions.

->The Sales table is connected to both the Books and Customers tables using foreign keys.

## 9. System Workflow

The general workflow of the system is:

Start
  |
  v
Main Menu
  |
  +----> Book Management
  |          |
  |          +--> Add
  |          +--> Update
  |          +--> Delete
  |          +--> Search
  |          +--> Display
  |
  +----> Customer Management
  |          |
  |          +--> Add
  |          +--> Update
  |          +--> Delete
  |          +--> Search
  |          +--> Display
  |
  +----> Sales & Billing
  |          |
  |          +--> Select Customer
  |          +--> Select Book
  |          +--> Enter Quantity
  |          +--> Calculate Total
  |          +--> Generate Bill
  |          +--> Update Stock
  |
  +----> Reports
  |          |
  |          +--> Inventory Report
  |          +--> Low Stock Report
  |          +--> Sales Report
  |          +--> Best Selling Books
  |
  v
Exit

## 10. Input and Output
Inputs

The system accepts:

Book details
Customer details
Book IDs
Customer IDs
Quantities
Prices
Search criteria
Menu choices
Outputs

The system displays:

Book records
Customer records
Bills
Sales history
Inventory information
Low-stock information
Sales statistics
Best-selling books

## 11. Validation and Error Handling

The project includes validation and error handling for common situations such as:

Empty input.
Invalid numbers.
Negative values.
Duplicate book IDs.
Duplicate customer IDs.
Non-existent books.
Non-existent customers.
Insufficient stock.
Attempting to delete records associated with existing sales.


## 12. Setup and How to Run the Project

### 12.1 Prerequisites

The following software is required:

- Python 3.x
- MySQL Server
- MySQL Shell or another MySQL client

The project also requires the Python package:

- mysql-connector-python

### 12.2 Install the Required Python Package

Open Command Prompt or a terminal and run:

```bash
pip install mysql-connector-python

### 12.3 Set Up the MySQL Database
Make sure MySQL Server is installed and running.
Open MySQL Shell or another MySQL client.
Open the database.sql file provided in this repository.
Execute the SQL commands in database.sql.
This creates the bookstore database and the required tables:
books
customers
sales
### 12.4 Configure the Database Connection

Open database.py.
Update the MySQL connection details according to the MySQL installation:

return mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="bookstore"
)

Replace YOUR_MYSQL_PASSWORD with the password configured for the MySQL root user.

Dont share or commit personal database passwords to GitHub.

### 12.5 Run the Application
Open the project folder in Command Prompt or a terminal.
Make sure the MySQL Server is running.
Run the following command:
python main.py

Alternatively, main.py can be opened and executed using Python IDLE.

### 12.6 Using the Application

After running main.py, the main menu is displayed.

The user can select:

Book Management
Customer Management
Sales & Billing
Reports
Exit

Follow the instructions displayed by the application to enter data and perform operations.

13. Conclusion

The Bookstore Management System provides a simple computerized solution for managing the basic operations of a bookstore. It demonstrates the practical use of Python programming, functions, conditional statements, loops, input validation, exception handling, SQL queries, database connectivity, and modular programming.
