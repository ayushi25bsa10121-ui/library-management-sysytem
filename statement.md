# Project Statement: Library Management System

## 1. Problem Statement
Many colleges and small libraries still use manual or semi-manual methods to manage book inventories and issue/return workflows. This causes misplaced books, incorrect availability information, and wasted time. Students and librarians need a simple, reliable system to manage books, track issues/returns, and maintain an up-to-date catalogue.

## 2. Scope of the Project
In scope:
- Maintain a catalogue of books (title, author, ISBN, number of copies).
- Register and manage library users (students).
- Issue and return books with validation and due date tracking.
- Persist data using JSON files for simplicity.
- Basic reporting: view all books, view available copies, view issued books.

Out of scope:
- Multi-branch synchronization
- Cloud backup and multi-device sync
- Payment/fine processing (optional future feature)
- Advanced authentication/roles

## 3. Target Users
- College students borrowing books
- Librarians managing inventory
- Departmental staff maintaining course materials

## 4. Objectives
- To build a simple, user-friendly library management tool.
- To allow librarians to add, update, delete, and search books.
- To enable registering users and issuing/returning books with validation.
- To persist data locally so records are retained across runs.
- To demonstrate modular programming, file I/O, and documentation skills.

## 5. High-Level Features
- Book Management: Add, update, delete, and search books.
- User Management: Register students and manage user details.
- Issue/Return: Issue books, track due dates, update availability on return.
- Reporting: View all books, available copies, and currently issued books.
- Persistence: Save/load using JSON files (books.json, users.json, issues.json).
