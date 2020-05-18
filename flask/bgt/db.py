import sqlite3
# con = sqlite3.connect("flask\\bgt\\bugs.db")
con = sqlite3.connect("bugs.db")
cursor = con.cursor()

bugs = []
cursor.execute("SELECT * FROM bugs WHERE id > -1")
for each_bug in cursor.fetchall():
    bugs.append(each_bug)

def get_bug_by_id(bug_id):
    cursor.execute("SELECT * FROM bugs WHERE id = ?", [(bug_id)])
    return cursor.fetchall()