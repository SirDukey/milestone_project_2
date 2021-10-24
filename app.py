import database


if __name__ == '__main__':
    prompt = """welcome to the library database
    a - add a book
    d - delete a book
    r - mark a book as read
    l - list all books
    q - quit
    please select an option: 
    """
    prompt_option = input(prompt)
    while prompt_option != 'q':
        if prompt_option == 'a':
            name = input('what is the name of the book: ')
            author = input('who is the author: ')
            database.add_book(name, author)
        elif prompt_option == 'd':
            name = input('which book would you like to delete: ')
            database.delete_book(name)
        elif prompt_option == 'r':
            name = input('which book have you read: ')
            database.mark_book_as_read(name)
        elif prompt_option == 'l':
            database.list_all_books()
        else:
            print('not a valid option')
        prompt_option = input(prompt)
