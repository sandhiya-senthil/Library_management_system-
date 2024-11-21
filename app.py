from flask import Flask, render_template, redirect, request, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'library_project'

# MySQL Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '9865'  # Your MySQL password here
app.config['MYSQL_DB'] = 'library_db'  # Your library database name here
mysql = MySQL(app)

# Route to render the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to display all available books
@app.route('/books')
def books():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books")  # Query to fetch all books
    books_info = cur.fetchall()
    cur.close()
    return render_template('books.html', books=books_info)

# Route to search books by ID, Title, or Author
@app.route('/search', methods=['POST', 'GET'])
def search():
    search_results = []
    if request.method == "POST":
        search_term = request.form['search_term']
        cur = mysql.connection.cursor()
        query = "SELECT * FROM books WHERE book_id LIKE %s OR title LIKE %s OR author LIKE %s"
        cur.execute(query, ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
        search_results = cur.fetchall()  # Fetch all matching results
        cur.close()
        return render_template('books.html', books=search_results)

# Route to insert a new book
@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == "POST":
        book_id = request.form['book_id']
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']
        stock_quantity = request.form['stock_quantity']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO books (book_id, title, author, price, stock_quantity) VALUES (%s, %s, %s, %s, %s)",
                    (book_id, title, author, price, stock_quantity))
        mysql.connection.commit()
        cur.close()
        flash("Book added successfully!", "success")
        return redirect(url_for('books'))

    return render_template('insert_book.html')

# Route to delete a book
@app.route('/delete/<string:book_id>', methods=['GET'])
def delete(book_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM books WHERE book_id=%s", (book_id,))
    mysql.connection.commit()
    cur.close()
    flash("Book deleted successfully!", "success")
    return redirect(url_for('books'))

# Route to edit book details (Display the Edit Form)
@app.route('/edit/<string:book_id>', methods=['GET'])
def edit(book_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books WHERE book_id=%s", (book_id,))
    book = cur.fetchone()  # Fetch the book details to edit
    cur.close()
    return render_template('edit_book.html', book=book)

# Route to handle the update of book details
@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        book_id = request.form['book_id']
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']
        stock_quantity = request.form['stock_quantity']
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE books SET title=%s, author=%s, price=%s, stock_quantity=%s WHERE book_id=%s",
                    (title, author, price, stock_quantity, book_id))
        mysql.connection.commit()
        cur.close()
        flash("Book updated successfully!", "success")
        return redirect(url_for('books'))

if __name__ == "__main__":
    app.run(debug=True)
