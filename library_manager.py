from typing import List, Optional, Dict
from datetime import datetime
from book import Book
from user import User
from storage import Storage

class LibraryManager:
    def __init__(self, storage: Storage):
        self.storage = storage
        self._load_data()

    def _load_data(self):
        self.books: List[Book] = [Book(**b) for b in self.storage.load_books()]
        self.users: List[User] = [User(**u) for u in self.storage.load_users()]
        self.issues: List[Dict] = self.storage.load_issues()

    def _save_all(self):
        self.storage.save_books([b.to_dict() for b in self.books])
        self.storage.save_users([u.to_dict() for u in self.users])
        self.storage.save_issues(self.issues)

    # Book operations
    def _next_book_id(self) -> int:
        return max((b.id for b in self.books), default=0) + 1

    def add_book(self, title: str, author: str, isbn: str, copies: int) -> Book:
        new = Book(id=self._next_book_id(), title=title, author=author, isbn=isbn, copies=copies)
        self.books.append(new)
        self._save_all()
        return new

    def find_books(self, keyword: str) -> List[Book]:
        kw = keyword.lower()
        return [b for b in self.books if kw in b.title.lower() or kw in b.author.lower() or kw in b.isbn.lower()]

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        for b in self.books:
            if b.id == book_id:
                return b
        return None

    def update_book(self, book_id: int, title: str, author: str, isbn: str, copies: int) -> bool:
        b = self.get_book_by_id(book_id)
        if not b:
            return False
        b.title = title
        b.author = author
        b.isbn = isbn
        b.copies = copies
        self._save_all()
        return True

    def delete_book(self, book_id: int) -> bool:
        b = self.get_book_by_id(book_id)
        if not b:
            return False
        # ensure not issued currently
        for issue in self.issues:
            if issue["book_id"] == book_id and not issue.get("returned", False):
                return False
        self.books.remove(b)
        self._save_all()
        return True

    # User operations
    def _next_user_id(self) -> int:
        return max((u.id for u in self.users), default=0) + 1

    def register_user(self, name: str, student_id: str) -> User:
        new = User(id=self._next_user_id(), name=name, student_id=student_id)
        self.users.append(new)
        self._save_all()
        return new

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        for u in self.users:
            if u.id == user_id:
                return u
        return None

    # Issue / Return operations
    def _next_issue_id(self) -> int:
        return max((i["issue_id"] for i in self.issues), default=0) + 1

    def issue_book(self, book_id: int, user_id: int, due_date_str: str) -> Optional[Dict]:
        book = self.get_book_by_id(book_id)
        user = self.get_user_by_id(user_id)
        if not book or not user:
            return None
        # check available copies
        issued_count = sum(1 for i in self.issues if i["book_id"] == book_id and not i.get("returned", False))
        available = book.copies - issued_count
        if available <= 0:
            return None
        # parse due date (YYYY-MM-DD)
        try:
            due = datetime.strptime(due_date_str, "%Y-%m-%d")
        except ValueError:
            return None
        issue = {
            "issue_id": self._next_issue_id(),
            "book_id": book_id,
            "user_id": user_id,
            "issued_on": datetime.now().strftime("%Y-%m-%d"),
            "due_date": due_date_str,
            "returned": False,
            "returned_on": None
        }
        self.issues.append(issue)
        self._save_all()
        return issue

    def return_book(self, issue_id: int) -> bool:
        for issue in self.issues:
            if issue["issue_id"] == issue_id and not issue.get("returned", False):
                issue["returned"] = True
                issue["returned_on"] = datetime.now().strftime("%Y-%m-%d")
                self._save_all()
                return True
        return False

    def list_all_books(self) -> List[Book]:
        return list(self.books)

    def list_issued(self) -> List[Dict]:
        return list(self.issues)
