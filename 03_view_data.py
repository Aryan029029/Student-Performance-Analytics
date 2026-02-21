import sqlite3

conn = sqlite3.connect("academic.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

print("Students Table:\n")
for row in rows:
    print(row)

conn.close()