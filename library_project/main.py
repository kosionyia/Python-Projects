from library_office import auth, books

def main():
    print(" ===== Welcome to Mr Bello's Library Window! ===== ")
    user = auth.authenticate()
    if user is None:
        return
    while True:
        request = input("Enter your request: ").strip()
        if request.upper() == "QUIT":
            break
        request_parts = request.split()

        if not request_parts:
            print("400 - I cannot read this slip.")
            continue

        if request_parts[0] == "GET":
            print("GET request")

        elif request_parts[0] == "POST":
            print("POST request")

        elif request_parts[0] == "PUT":
            print("PUT request")

        elif request_parts[0] == "DELETE":
            print("DELETE request")

        else:
            print("400 — I cannot read this slip.")



def show_book(book):
    """Display a book in a readable format"""
    print(
        f"{book['id']}. {book['title']} - "
        f"{book['author']} - ({book['status']})"
    )


def show_books(books):
    """Display a list of books in a readable format"""
    for book in books:
        show_book(book)