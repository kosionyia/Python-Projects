from library_office.auth import authenticate, can_delete
from library_office.books import (
    get_books,
    get_book,
    add_book,
    update_book,
    delete_book,
    get_borrowed_books
)


def show_book(book):
    print(
        f"{book['id']}. {book['title']} - "
        f"{book['author']} - {book['status']}"
    )


def main():
    print("=== Mr. Bello's Library Window ===")

    user = authenticate()

    if user is None:
        return

    while True:
        request = input("\nEnter request: ").strip()

        if request.upper() == "QUIT":
            print("200 - Window closed.")
            break

        request_parts = request.split()

        if not request_parts:
            print("\n400 - I cannot read this slip.")
            continue

        verb = request_parts[0]

        """ GET method conditional"""

        if verb == "GET":

            if len(request_parts) == 2 and request_parts[1] == "books":
                books = get_books()

                for book in books:
                    show_book(book)

                print("\n200 - Done, here you go.")

            elif len(request_parts) == 3 and request_parts[1] == "books" and request_parts[2] == "borrowed":
                books = get_borrowed_books()

                for book in books:
                    show_book(book)

                print("\n200 - Done, here you go.")

            elif len(request_parts) == 3 and request_parts[1] == "book":
                try:
                    book_id = int(request_parts[2])
                except ValueError:
                    print("\n400 - I cannot read this slip.")
                    continue

                book = get_book(book_id)

                if book is None:
                    print("\n404 - There is no such book.")
                else:
                    show_book(book)
                    print("\n200 - Done, here you are.")

            else:
                print("\n400 - I cannot read this slip.")

            """ POST method conditional"""
        elif verb == "POST":

            if len(request_parts) != 2 or request_parts[1] != "book":
                print("\n400 - I cannot read this slip.")
                continue

            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()
            status = input("Enter status (on shelf/borrowed): ").strip().lower()

            if not title or not author:
                print("\n400 - I cannot read this slip.")
                continue

            if status not in ["on shelf", "borrowed"]:
                print("\n400 - I cannot read this slip.")
                continue

            book = add_book(title, author, status)

            show_book(book)
            print("201 - Created - a new thing now exists.")

            """ PUT method conditional"""
        elif verb == "PUT":

            if len(request_parts) != 3 or request_parts[1] != "book":
                print("\n400 - I cannot read this slip.")
                continue

            try:
                book_id = int(request_parts[2])
            except ValueError:
                print("\n400 - I cannot read this slip.")
                continue

            title = input("Enter new title: ").strip()
            author = input("Enter new author: ").strip()
            status = input("Enter new status (on shelf/borrowed): ").strip().lower()

            if not title or not author:
                print("\n400 - I cannot read this slip.")
                continue

            if status not in ["on shelf", "borrowed"]:
                print("\n400 - I cannot read this slip.")
                continue

            book = update_book(book_id, title, author, status)

            if book is None:
                print("404 - There is no such book.")
            else:
                show_book(book)
                print("200 - Done, here you are.")

                """DELETE method conditional"""
        elif verb == "DELETE":

            if len(request_parts) != 3 or request_parts[1] != "book":
                print("\n400 - I cannot read this slip.")
                continue

            try:
                book_id = int(request_parts[2])
            except ValueError:
                print("\n400 - I cannot read this slip.")
                continue

            if not can_delete(user):
                print("403 - I know who you are, and you are not allowed to do this.")
                continue

            book = delete_book(book_id)

            if book is None:
                print("404 - There is no such book.")
            else:
                show_book(book)
                print("200 - Done, here you are.")

       
        else:
            print("\n400 - I cannot read this slip.")


if __name__ == "__main__":
    main()