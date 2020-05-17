import sqlite3
connect_db = sqlite3.connect("flask\\bgt\\bugs.db")
cursor = connect_db.cursor()

cursor.execute("""CREATE TABLE bugs (id integer, status integer, title text, description text, psw str)""")
connect_db.commit()
print("Configuration of bugs' database is ended. File called 'bugs.db'. Please, do not touch it because it may cause an error")