import sqlite3, datetime
from flask import Flask, render_template, request
app = Flask(__name__)

# tell Flask what URL should trigger our function.
@app.route('/books')
def index():
	html_page = 'books.html'
	conn = sqlite3.connect('TestDB.db')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Books')  
	return render_template(html_page, items = cursor.execute('SELECT * FROM Books').fetchall())

# calling to run URL
if __name__ == "__main__":
    app.run()