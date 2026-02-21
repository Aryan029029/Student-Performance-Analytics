import sqlite3

# Connect to database (creates academic.db file if it doesn't exist)
conn = sqlite3.connect("academic.db")
cursor = conn.cursor()

# Drop tables if they already exist (so we start fresh)
cursor.execute("DROP TABLE IF EXISTS marks")
cursor.execute("DROP TABLE IF EXISTS attendance")
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("DROP TABLE IF EXISTS subjects")

# -------------------------------
# STUDENTS TABLE
# -------------------------------
cursor.execute("""
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    semester INTEGER NOT NULL
)
""")

# -------------------------------
# SUBJECTS TABLE
# -------------------------------
cursor.execute("""
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL
)
""")

# -------------------------------
# MARKS TABLE
# -------------------------------
cursor.execute("""
CREATE TABLE marks (
    mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    marks INTEGER CHECK(marks BETWEEN 0 AND 100),
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(subject_id) REFERENCES subjects(subject_id)
)
""")

# -------------------------------
# ATTENDANCE TABLE
# -------------------------------
cursor.execute("""
CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    attendance_percentage REAL CHECK(attendance_percentage BETWEEN 0 AND 100),
    FOREIGN KEY(student_id) REFERENCES students(student_id)
)
""")

# Save changes and close
conn.commit()
conn.close()

print("Academic database created successfully!")