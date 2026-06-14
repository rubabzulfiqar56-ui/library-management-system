FILE = "data/students.txt"

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    if sid == "" or name == "":
        print("Fields cannot be empty!")
        return

    with open(FILE, "a") as f:
        f.write(f"{sid},{name}\n")

    print("Student Added Successfully")


def view_students():
    try:
        with open(FILE, "r") as f:
            data = f.read()

            if data:
                print("\n===== STUDENTS =====")
                print(data)
            else:
                print("No students found")

    except FileNotFoundError:
        print("Student file not found")


def update_student():
    print("Update Student Feature")


def delete_student():
    print("Delete Student Feature")


def student_menu():
    while True:
        print("\n===== STUDENT MODULE =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid Choice")