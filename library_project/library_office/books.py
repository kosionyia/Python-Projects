import storage

def get_books():
    """ Return all the books in the library """
    return storage.load_data()


def get_book(book_id):
    """ return a book by its id """

    books = storage.load_data()
    for book in books:
        if book["id"] == book_id:
            return book
    return None


def add_book(title, author, status):
    """ Add a new book to the library"""
    books = storage.load_data()
    if books:
        new_id = max(book["id"] for book in books) + 1
    else:
        new_id = 1
    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "status": status
    }

    books.append(new_book)
    storage.save_data(books)

    return new_book


def update_book(book_id, title, author, status):
    """Update an existing book, save and return it.
    """
    books = storage.load_data()

    for book in books:
        if  book["id"] == book_id:
            book["title"] = title
            book["author"] = author
            book["status"] = status

            storage.save_data(books)
            return book

    return None


def delete_book(book_id):
    """Delete a book, save and return it.
    """

    books = storage.load_data()

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            storage.save_data(books)

            return book

    return None         


def get_borrowed_books():
    """Return only books that the staus is borrowed."""

    books = storage.load_data()

    return [
        book for book in books
        if book["status"] == "borrowed"
    ]



if __name__ == "__main__":
    print(get_books())
