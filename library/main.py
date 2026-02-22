from library.library_system import LibrarySystem

def menu():
    print("\n===== Smart Library Management System =====")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add Member")
    print("4. List Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("0. Exit")

def main():
    system = LibrarySystem()

    while True:
        menu()
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")
                system.add_book(title, author, isbn)
                print("Book added successfully!")

            elif choice == "2":
                books = system.list_books()
                for book in books:
                    print(book)

            elif choice == "3":
                member_id = input("Member ID: ")
                name = input("Name: ")
                system.add_member(member_id, name)
                print("Member added successfully!")

            elif choice == "4":
                members = system.list_members()
                for member in members:
                    print(member)

            elif choice == "5":
                isbn = input("ISBN: ")
                member_id = input("Member ID: ")
                system.borrow_book(isbn, member_id)
                print("Book borrowed successfully!")

            elif choice == "6":
                isbn = input("ISBN: ")
                system.return_book(isbn)
                print("Book returned successfully!")

            elif choice == "0":
                print("Exiting program.")
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)

if _name_ == "_main_":
    main()
