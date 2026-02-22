class Book:
    def _init_(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True

    def _str_(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.title} by {self.author} ({status})"
