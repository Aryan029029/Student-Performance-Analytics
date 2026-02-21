import sqlite3

conn = sqlite3.connect("academic.db")
cursor = conn.cursor()

query = """
SELECT students.name, AVG(marks.marks)
FROM students
JOIN marks ON students.student_id = marks.student_id
GROUP BY students.student_id
ORDER BY AVG(marks.marks) DESC
"""

cursor.execute(query)
rows = cursor.fetchall()

print("\nAverage Marks:\n")

for row in rows:
    print(f"{row[0]} → {round(row[1], 2)}")

conn.close()