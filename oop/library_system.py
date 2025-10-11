class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, num):
        super().__init__(title, author)
        self.num = num

    def file_size(self):
        print(f"size: {self.num}")

    def __repr__(self):
        return f"EBook: {self.title} by {self.author} File Size: {self.num}"


class PrintBook(Book):
    def __init__(self, title, author, page):
        super().__init__(title, author)
        self.page = page

    def file_size(self):
        print(f"page num {self.page}")

    def __repr__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page}"


class Library:
    def __init__(self):
        self.book = []

    def add_book(self, book):
        self.book.append(book)

    def list_books(self):
        for book in self.book:
            print(repr(book))


        