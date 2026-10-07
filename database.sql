-- Create the bookstore database if it does not already exist
CREATE DATABASE IF NOT EXISTS bookstore;

-- Select the bookstore database for use
USE bookstore;


-- Books table
-- Stores information about all books available in the bookstore
CREATE TABLE IF NOT EXISTS books (
    -- Unique ID for each book
    book_id INT PRIMARY KEY AUTO_INCREMENT,

    -- Name of the book
    book_name VARCHAR(100) NOT NULL,

    -- Name of the author
    author VARCHAR(100) NOT NULL,

    -- Name of the publisher
    publisher VARCHAR(100),

    -- Category or genre of the book
    category VARCHAR(50),

    -- Price of the book
    price DECIMAL(10,2) NOT NULL,

    -- Number of copies available
    quantity INT NOT NULL
);


-- Customers table
-- Stores information about bookstore customers
CREATE TABLE IF NOT EXISTS customers (
    -- Unique ID for each customer
    customer_id INT PRIMARY KEY AUTO_INCREMENT,

    -- Name of the customer
    customer_name VARCHAR(100) NOT NULL,

    -- Phone number of the customer
    phone VARCHAR(15),

    -- Email address of the customer
    email VARCHAR(100)
);


-- Sales table
-- Stores information about each book sale
CREATE TABLE IF NOT EXISTS sales (
    -- Unique ID for each sale
    sale_id INT PRIMARY KEY AUTO_INCREMENT,

    -- ID of the customer who made the purchase
    customer_id INT NOT NULL,

    -- ID of the book that was purchased
    book_id INT NOT NULL,

    -- Number of copies purchased
    quantity INT NOT NULL,

    -- Total amount of the sale
    total_amount DECIMAL(10,2) NOT NULL,

    -- Date on which the sale was made
    sale_date DATE NOT NULL DEFAULT (CURRENT_DATE),

    -- Connect customer_id with the customers table
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    -- Connect book_id with the books table
    FOREIGN KEY (book_id)
        REFERENCES books(book_id)
);
