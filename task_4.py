import sqlite3

# create table into database
def create_table(conn):
	cursor = conn.cursor()
	sql ='''CREATE TABLE BOOKS(
	id INT,
	author TEXT,
	title TEXT,
	created TEXT
	)'''
	cursor.execute(sql)
	conn.commit()

# main function
def main():
	conn = sqlite3.connect('TestDB.db')
	create_table(conn)
	conn.close()

# calling main()
if __name__ == "__main__":
    main()