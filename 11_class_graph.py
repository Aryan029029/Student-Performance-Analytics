import sqlite3
import matplotlib.pyplot as plt

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
data = cursor.fetchall()

names = [row[0] for row in data]
averages = [round(row[1],2) for row in data]

plt.figure(figsize=(8,5))
bars = plt.bar(names, averages)

plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Class Performance Analysis")
plt.ylim(0,100)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1,
             f"{height}", ha='center')

plt.tight_layout()
plt.show()

conn.close()