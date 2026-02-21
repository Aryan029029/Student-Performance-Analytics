import sqlite3

conn = sqlite3.connect("academic.db")
cursor = conn.cursor()

query = """
SELECT students.name, marks.subject_id, marks.marks
FROM students
JOIN marks ON students.student_id = marks.student_id
ORDER BY students.name
"""

cursor.execute(query)
rows = cursor.fetchall()

print("\nStudent Marks:\n")

for row in rows:
    print(f"Name: {row[0]} | Subject: {row[1]} | Marks: {row[2]}")

conn.close()