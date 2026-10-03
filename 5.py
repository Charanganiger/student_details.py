students = []

def add_student():
    student = {
        "id": input("Enter Student ID: "),
        "name": input("Enter Student Name: "),
        "age": input("Enter Age: "),
        "class": input("Enter Class: "),
        "gender": input("Enter Gender: "),
        "phone": input("Enter Phone Number: "),
        "marks": float(input("Enter Marks: "))
    }

    students.append(student)
    print("\nStudent added successfully!\n")


def display_students():
    if not students:
        print("\nNo student records found.\n")
        return

    for student in students:
        print("\n--- Student Details ---")
        for key, value in student.items():
            print(f"{key.title()}: {value}")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")