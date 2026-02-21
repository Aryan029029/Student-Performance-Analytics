import sqlite3

conn = sqlite3.connect("academic.db")
cursor = conn.cursor()

# Check actual column names inside marks table
cursor.execute("PRAGMA table_info(marks)")
columns = cursor.fetchall()

column_names = [col[1] for col in columns]

# Find correct subject column name automatically
if "subject" in column_names:
    subject_column = "subject"
else:
    # find the third column (usually subject position)
    subject_column = column_names[2]

# Insert marks
cursor.execute(f"INSERT INTO marks (student_id, {subject_column}, marks) VALUES (1, 'Maths', 85)")
cursor.execute(f"INSERT INTO marks (student_id, {subject_column}, marks) VALUES (1, 'Physics', 78)")
cursor.execute(f"INSERT INTO marks (student_id, {subject_column}, marks) VALUES (2, 'Maths', 90)")
cursor.execute(f"INSERT INTO marks (student_id, {subject_column}, marks) VALUES (2, 'Physics', 88)")
cursor.execute(f"INSERT INTO marks (student_id, {subject_column}, marks) VALUES (3, 'Maths', 72)")
cursor.execute(f"INSERT INTO marks (student_id, {subject_column}, marks) VALUES (3, 'Physics', 75)")
cursor.execute(f"INSERT INTO marks (student_id, {subject_column}, marks) VALUES (4, 'Maths', 60)")
cursor.execute(f"INSERT INTO marks (student_id, {subject_column}, marks) VALUES (4, 'Physics', 65)")
cursor.execute(f"INSERT INTO marks (student_id, {subject_column}, marks) VALUES (5, 'Maths', 95)")
cursor.execute(f"INSERT INTO marks (student_id, {subject_column}, marks) VALUES (5, 'Physics', 92)")

conn.commit()
conn.close()

print("Marks inserted successfully!")