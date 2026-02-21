import sqlite3

def connect():
    return sqlite3.connect("academic.db")

def view_topper():
    conn = connect()
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
    result = cursor.fetchone()

    if result:
        print(f"\n🏆 Topper: {result[0]} with average {round(result[1],2)}")
    else:
        print("No data found.")

    conn.close()


def student_report():
    conn = connect()
    cursor = conn.cursor()

    name = input("\nEnter student name: ")

    query = """
    SELECT students.name, marks.subject_id, marks.marks
    FROM students
    JOIN marks ON students.student_id = marks.student_id
    WHERE students.name = ?
    """

    cursor.execute(query, (name,))
    rows = cursor.fetchall()

    if rows:
        print(f"\nReport for {name}:\n")
        total = 0

        for row in rows:
            print(f"Subject: {row[1]} | Marks: {row[2]}")
            total += row[2]

        print("Average:", round(total/len(rows),2))
    else:
        print("Student not found.")

    conn.close()


def department_average():
    conn = connect()
    cursor = conn.cursor()

    query = """
    SELECT students.department, AVG(marks.marks)
    FROM students
    JOIN marks ON students.student_id = marks.student_id
    GROUP BY students.department
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print("\nDepartment Averages:\n")
    for row in rows:
        print(f"{row[0]} → {round(row[1],2)}")

    conn.close()


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. View Topper")
    print("2. Student Report")
    print("3. Department Average")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_topper()
    elif choice == "2":
        student_report()
    elif choice == "3":
        department_average()
    elif choice == "4":
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Try again.")