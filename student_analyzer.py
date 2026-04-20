import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks INTEGER
)
""")

def add_student(name, marks):
    cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
    conn.commit()

def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def calculate_average():
    cursor.execute("SELECT AVG(marks) FROM students")
    avg = cursor.fetchone()[0]
    print(f"Average Marks: {avg:.2f}")

def rank_students():
    cursor.execute("SELECT name, marks FROM students ORDER BY marks DESC")
    data = cursor.fetchall()
    print("\nStudent Rankings:")
    for i, row in enumerate(data, start=1):
        print(f"Rank {i}: {row[0]} - {row[1]} marks")

def assign_grades():
    cursor.execute("SELECT name, marks FROM students")
    print("\nGrades:")
    for name, marks in cursor.fetchall():
        if marks >= 90:
            grade = 'A'
        elif marks >= 75:
            grade = 'B'
        elif marks >= 60:
            grade = 'C'
        else:
            grade = 'D'
        print(f"{name}: {marks} -> Grade {grade}")

while True:
    print("\n--- Student Performance Analyzer ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Average Marks")
    print("4. Rank Students")
    print("5. Assign Grades")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        add_student(name, marks)

    elif choice == '2':
        view_students()

    elif choice == '3':
        calculate_average()

    elif choice == '4':
        rank_students()

    elif choice == '5':
        assign_grades()

    elif choice == '6':
        break

    else:
        print("Invalid choice!")

conn.close()
