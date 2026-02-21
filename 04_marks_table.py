import sqlite3

conn = sqlite3.connect("academic.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject TEXT,
    marks INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id)
)
""")

print("Marks table created successfully!")

conn.commit()
conn.close()