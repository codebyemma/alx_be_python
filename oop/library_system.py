class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

class EBook(Book):
    def __init__(self, title, author, num):
        super()__init__(title, author)
        self.num = num

    def file_size(self):
        print(f"size: {self.num}")

    def __repr__(self):
        return f"EBook('{self.title}' by '{self.author}' File Size: )"


class PrintBook(Book):
    def __init__(self, title, author, page):
        super()__init__(title, author)
        self.page = page

    def file_size(self):
        print(f"page num {self.page}")

    def __repr__(self):
        return f"PrintBook('{self.title}' by '{self.author}' Page Count: '{self.page}')"


class Library:
    def __init__(self, book):
        self.book = book

    def add_book(self, book):
        self.book.push(book)

    def list_books(self):
        for book in self.book:
            print(repr(book))


        