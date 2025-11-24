# Library Management System

## Overview
A simple Library Management System (LMS) to help students and librarians manage books, issue/return operations, and view inventory. This CLI-based Python application allows adding books, searching, issuing books to users, returning books, and generating simple reports. Data is stored in JSON files so no database setup is required.

## Features
- Add / Update / Delete book records
- Search books by title, author, or ISBN
- Register users (students)
- Issue book to a user and return book functionality
- View all books and view issued books
- Save and load data using JSON (`books.json`, `users.json`, `issues.json`)
- Simple validation and error messages

## Technologies / Tools Used
- Python 3.x
- JSON for storage
- Git / GitHub for version control
- (Optional) Visual Studio Code or any text editor

## Repository Structure
library-management-system/
├── main.py
├── ui.py
├── book.py
├── user.py
├── library_manager.py
├── storage.py
├── books.json
├── users.json
├── issues.json
├── README.md
└── statement.md
