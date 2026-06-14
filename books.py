FILE = "data/books.txt"

def add_book():
    bid = input("Enter Book ID: ")
    title = input("Enter Book Title: ")

    if bid == "" or title == "":
        print("Fields cannot be empty!")
        return

    with open(FILE, "a") as f:
        f.write(f"{bid},{title}\n")

    print("Book Added Successfully")


def view_books():
    try:
        with open(FILE, "r") as f:
            data = f.read()

            if data:
                print("\n===== BOOKS =====")
                print(data)
            else:
                print("No books found")

    except FileNotFoundError:
        print("Books file not found")


def update_book():
    print("Update Book Feature")


def delete_book():
    print("Delete Book Feature")


def book_menu():
    while True:
        print("\n===== BOOK MODULE =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            break
        else:
            print("Invalid Choice")