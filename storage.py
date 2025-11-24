import json
import os
from typing import List, Dict

DEFAULT_BOOKS = "books.json"
DEFAULT_USERS = "users.json"
DEFAULT_ISSUES = "issues.json"

class Storage:
    def __init__(self, books_file=DEFAULT_BOOKS, users_file=DEFAULT_USERS, issues_file=DEFAULT_ISSUES):
        self.books_file = books_file
        self.users_file = users_file
        self.issues_file = issues_file
        # ensure files exist
        for f in (self.books_file, self.users_file, self.issues_file):
            if not os.path.exists(f):
                with open(f, "w", encoding="utf-8") as fh:
                    json.dump([], fh)

    def load(self, filename: str) -> List[Dict]:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, filename: str, data: List[Dict]) -> None:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    # books
    def load_books(self) -> List[Dict]:
        return self.load(self.books_file)

    def save_books(self, books: List[Dict]) -> None:
        self.save(self.books_file, books)

    # users
    def load_users(self) -> List[Dict]:
        return self.load(self.users_file)

    def save_users(self, users: List[Dict]) -> None:
        self.save(self.users_file, users)

    # issues
    def load_issues(self) -> List[Dict]:
        return self.load(self.issues_file)

    def save_issues(self, issues: List[Dict]) -> None:
        self.save(self.issues_file, issues)
