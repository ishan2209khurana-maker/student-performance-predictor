
library = {}

while True:
    print("\n--- Library Record Management System ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Display All Books")
    print("4. Delete Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        book_name = input("Enter Book Name: ")

        library[book_id] = book_name
        print("Book added successfully!")

    elif choice == 2:
        book_id = int(input("Enter Book ID to search: "))

        if book_id in library:
            print("Book Found:", library[book_id])
        else:
            print("Book Not Found!")

    elif choice == 3:
        print("\nLibrary Records:")

        for book_id, book_name in library.items():
            print(book_id, ":", book_name)

        if not library:
            print("No records available!")

    elif choice == 4:
        book_id = int(input("Enter Book ID to delete: "))

        if book_id in library:
            del library[book_id]
            print("Book deleted successfully!")
        else:
            print("Book Not Found!")

    elif choice == 5:
        print("Exiting Library System...")
        break

    else:
        print("Invalid Choice!")
