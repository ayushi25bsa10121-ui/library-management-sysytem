from storage import Storage
from library_manager import LibraryManager
from ui import show_menu, handle_choice

def main():
    storage = Storage()
    lm = LibraryManager(storage)
    while True:
        show_menu()
        choice = input("Enter choice (1-10): ").strip()
        should_exit = handle_choice(choice, lm)
        if should_exit:
            break

if __name__ == "__main__":
    main()
