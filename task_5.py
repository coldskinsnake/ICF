import sqlite3, datetime
from flask import Flask, render_template, request
app = Flask(__name__)

# extract and increment last ID
def read_table(cursor):

	# extract last row content
	sqlite_select_query = """SELECT * from Books ORDER BY ID DESC LIMIT 1"""
	cursor.execute(sqlite_select_query)
	records = cursor.fetchone()
	
	# if database empty, then intialize value
	if records:
		incremented_id = records[0] + 1

	# otherwise increment
	else:
		incremented_id = 0

	return incremented_id

# display contents of table
def print_table(conn):
	cur = conn.cursor()
	print("Printing Table:")
	with conn:
		cur.execute("SELECT * FROM BOOKS")
		print(cur.fetchall())

# insert data into table
def insert_table(extracted_author,extracted_title):

	# connect to a sqlite db instance locally
	conn = sqlite3.connect('TestDB.db')
	cursor = conn.cursor()

	# get incremeted id and current datetime
	incremented_id = read_table(cursor)
	get_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	# update rows
	rows = [(incremented_id, extracted_author, extracted_title, get_time)]
	cursor.executemany('insert into BOOKS values (?,?,?,?)', rows)	
	conn.commit()
	cursor.close()
	print_table(conn)

# tell Flask what URL should trigger our function.
@app.route('/create_book', methods=['GET', 'POST'])
def index():
	html_page = 'create_book.html'

	# if user clicks submit
	if request.method == 'POST':	
		extracted_author = request.form.get('author')
		extracted_title = request.form.get('title')
		insert_table(extracted_author,extracted_title)
		return render_template(html_page)
	
	# if user access URL
	if request.method == 'GET':	
		return render_template(html_page)

# calling to run URL
if __name__ == "__main__":
    app.run()