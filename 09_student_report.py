import sqlite3

conn = sqlite3.connect("academic.db")
cursor = conn.cursor()

name_input = input("Enter student name: ")

query = """
SELECT students.name, marks.subject_id, marks.marks
FROM students
JOIN marks ON students.student_id = marks.student_id
WHERE students.name = ?
"""

cursor.execute(query, (name_input,))
rows = cursor.fetchall()

if rows:
    print(f"\nReport for {name_input}:\n")
    total = 0
    count = 0

    for row in rows:
        print(f"Subject: {row[1]} | Marks: {row[2]}")
        total += row[2]
        count += 1

    print("\nAverage:", round(total / count, 2))
else:
    print("Student not found.")

conn.close()