import sqlite3
con = sqlite3.connect("flask\\bgt\\bugs.db")
cursor = con.cursor()

test_data = [(0, 4, "Bug title", """Bug description""", "123"),
             (1, 2, "Bug title", """Bug description""", "123"),
             (2, 0, "Bug title", """Bug description""", "123"),
             (3, 3, "Bug title", """Bug description""", "123"),
             (4, 1, "Bug title", """Bug description""", "123")]

cursor.executemany("INSERT INTO bugs VALUES (?,?,?,?,?)", test_data)
con.commit()

print("Test data sucessfully pushed into database 'bugs.db'.")