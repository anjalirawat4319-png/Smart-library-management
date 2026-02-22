from library.book import Book
from library.member import Member
import json
import os

class LibrarySystem:
    def _init_(self):
        self.books = []      # list of Book objects
        self.members = []    # list of Member objects
        self.data_file = "data.json"
        self.load_data()

    # ---------------- Books ----------------
    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_data()

    def list_books(self):
        return self.books

    def find_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    # ---------------- Members ----------------
    def add_member(self, member_id, name):
        self.members.append(Member(member_id, name))
        self.save_data()

    def list_members(self):
        return self.members

    def find_member(self, member_id):
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None

    # ---------------- Borrow / Return ----------------
    def borrow_book(self, isbn, member_id):
        book = self.find_book(isbn)
        member = self.find_member(member_id)

        if book is None:
            raise ValueError("Book not found.")
        if member is None:
            raise ValueError("Member not found.")

        ok = book.borrow()
        if not ok:
            raise ValueError("Book is already borrowed.")

        self.save_data()

    def return_book(self, isbn):
        book = self.find_book(isbn)
        if book is None:
            raise ValueError("Book not found.")
        book.return_book()
        self.save_data()

    # ---------------- Save / Load (JSON) ----------------
    def save_data(self):
        data = {
            "books": [
                {
                    "title": b.title,
                    "author": b.author,
                    "isbn": b.isbn,
                    "is_available": b.is_available
                }
                for b in self.books
            ],
            "members": [
                {
                    "member_id": m.member_id,
                    "name": m.name
                }
                for m in self.members
            ]
        }

        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load_data(self):
        if not os.path.exists(self.data_file):
            return

        with open(self.data_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.books = []
        for b in data.get("books", []):
            book = Book(b["title"], b["author"], b["isbn"])
            book.is_available = b.get("is_available", True)
            self.books.append(book)

        self.members = []
        for m in data.get("members", []):
            self.members.append(Member(m["member_id"], m["name"]))
