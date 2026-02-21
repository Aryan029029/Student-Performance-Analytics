import sqlite3
import random

conn = sqlite3.connect("academic.db")
cursor = conn.cursor()

# -------------------------------
# INSERT STUDENTS
# -------------------------------
students = [
    ("Aryan", "CSE", 1),
    ("Raghav", "CSE", 1),
    ("Prisha", "ECE", 1),
    ("Pria", "ECE", 1),
    ("Neha", "CSE", 1)
]

cursor.executemany(
    "INSERT INTO students (name, department, semester) VALUES (?, ?, ?)",
    students
)

# -------------------------------
# INSERT SUBJECTS
# -------------------------------
subjects = [
    ("Mathematics",),
    ("Physics",),
    ("Programming",)
]

cursor.executemany(
    "INSERT INTO subjects (subject_name) VALUES (?)",
    subjects
)

# -------------------------------
# INSERT MARKS (Random)
# -------------------------------
for student_id in range(1, 6):
    for subject_id in range(1, 4):
        cursor.execute(
            "INSERT INTO marks (student_id, subject_id, marks) VALUES (?, ?, ?)",
            (student_id, subject_id, random.randint(50, 100))
        )

# -------------------------------
# INSERT ATTENDANCE
# -------------------------------
for student_id in range(1, 6):
    cursor.execute(
        "INSERT INTO attendance (student_id, attendance_percentage) VALUES (?, ?)",
        (student_id, random.randint(60, 100))
    )

conn.commit()
conn.close()

print("Sample data inserted successfully!")