import sqlite3

conn = sqlite3.connect("academic.db")
cursor = conn.cursor()

query = """
SELECT students.name, AVG(marks.marks) AS avg_marks
FROM students
JOIN marks ON students.student_id = marks.student_id
GROUP BY students.student_id
ORDER BY avg_marks DESC
LIMIT 1
"""

cursor.execute(query)
topper = cursor.fetchone()

print("\nTopper:\n")
print(f"{topper[0]} with average {round(topper[1], 2)}")

conn.close()