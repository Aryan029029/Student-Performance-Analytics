import sqlite3

conn = sqlite3.connect("academic.db")
cursor = conn.cursor()

# remove duplicate rows
cursor.execute("""
DELETE FROM marks
WHERE mark_id NOT IN (
    SELECT MIN(mark_id)
    FROM marks
    GROUP BY student_id, subject_id, marks
)
""")

conn.commit()
conn.close()

print("Duplicates cleaned.")