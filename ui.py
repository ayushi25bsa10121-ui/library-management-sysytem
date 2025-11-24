from library_manager import LibraryManager
from storage import Storage
from datetime import datetime

def print_book(b):
    print(f"[{b.id}] {b.title} — {b.author} (ISBN:{b.isbn}) copies:{b.copies}")

def print_issue(i):
    status = "Returned" if i.get("returned", False) else "Issued"
    print(f"[Issue {i['issue_id']}] BookID:{i['book_id']} UserID:{i['user_id']} Issued:{i['issued_on']} Due:{i['due_date']} Status:{status}")

def show_menu():
    print("\n==== Library Management System ====")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. Search Books")
    print("5. Register User")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. View All Books")
    print("9. View Issued Books")
    print("10. Exit")

def handle_choice(choice: str, lm: LibraryManager):
    if choice == "1":
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        isbn = input("ISBN: ").strip()
        try:
            copies = int(input("Number of copies: ").strip())
        except ValueError:
            print("Invalid copies number.")
            return False
        new = lm.add_book(title, author, isbn, copies)
        print("Added book with ID:", new.id)

    elif choice == "2":
        try:
            bid = int(input("Book ID to update: ").strip())
        except ValueError:
            print("Invalid ID.")
            return False
        b = lm.get_book_by_id(bid)
        if not b:
            print("Book not found.")
            return False
        title = input(f"New title (current: {b.title}): ").strip() or b.title
        author = input(f"New author (current: {b.author}): ").strip() or b.author
        isbn = input(f"New ISBN (current: {b.isbn}): ").strip() or b.isbn
        try:
            copies = input(f"New copies (current: {b.copies}): ").strip()
            copies = int(copies) if copies else b.copies
        except ValueError:
            print("Invalid copies.")
            return False
        if lm.update_book(bid, title, author, isbn, copies):
            print("Book updated.")
        else:
            print("Failed to update.")

    elif choice == "3":
        try:
            bid = int(input("Book ID to delete: ").strip())
        except ValueError:
            print("Invalid ID.")
            return False
        ok = lm.delete_book(bid)
        if ok:
            print("Book deleted.")
        else:
            print("Cannot delete. Maybe book is issued or not exists.")

    elif choice == "4":
        kw = input("Enter title/author/ISBN to search: ").strip()
        res = lm.find_books(kw)
        if not res:
            print("No books found.")
        else:
            for b in res:
                print_book(b)

    elif choice == "5":
        name = input("User name: ").strip()
        sid = input("Student ID: ").strip()
        new = lm.register_user(name, sid)
        print("Registered user with ID:", new.id)

    elif choice == "6":
        try:
            bid = int(input("Book ID to issue: ").strip())
            uid = int(input("User ID: ").strip())
        except ValueError:
            print("Invalid IDs.")
            return False
        due = input("Due date (YYYY-MM-DD): ").strip()
        issue = lm.issue_book(bid, uid, due)
        if issue:
            print("Issued, Issue ID:", issue["issue_id"])
        else:
            print("Issue failed. Check book availability, user ID, or due date format (YYYY-MM-DD).")

    elif choice == "7":
        try:
            iid = int(input("Issue ID to return: ").strip())
        except ValueError:
            print("Invalid ID.")
            return False
        ok = lm.return_book(iid)
        if ok:
            print("Book returned successfully.")
        else:
            print("Return failed. Check Issue ID.")

    elif choice == "8":
        for b in lm.list_all_books():
            print_book(b)

    elif choice == "9":
        for i in lm.list_issued():
            print_issue(i)

    elif choice == "10":
        print("Goodbye!")
        return True

    else:
        print("Invalid choice.")
    return False
