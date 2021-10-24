books = []


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]


def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True


def list_all_books():
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")
