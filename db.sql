-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS library_db;

-- Use the library_db database
USE library_db;

-- Create the books table
CREATE TABLE IF NOT EXISTS books (
    book_id INT PRIMARY KEY,            -- Book ID (Primary Key)
    title VARCHAR(255) NOT NULL,        -- Title of the book
    author VARCHAR(255) NOT NULL,       -- Author of the book
    price DECIMAL(10, 2) NOT NULL,      -- Price of the book (e.g., 99.99)
    stock_quantity INT NOT NULL         -- Quantity of the book in stock
);

-- Optional: Insert some sample data into the books table
INSERT INTO books (book_id, title, author, price, stock_quantity)
VALUES
    (1, 'The Great Gatsby', 'F. Scott Fitzgerald', 10.99, 50),
    (2, '1984', 'George Orwell', 9.99, 30),
    (3, 'To Kill a Mockingbird', 'Harper Lee', 12.99, 40),
    (4, 'Moby-Dick', 'Herman Melville', 14.50, 20),
    (5, 'Pride and Prejudice', 'Jane Austen', 11.99, 15);

-- Verify the table creation and data insertion
SELECT * FROM books;
