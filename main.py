def main():

    # books to read
    book_name = "books/frankenstein.txt"
    get_book_text(book_name)



def get_book_text(book_name):
    with open(book_name) as f:
        book_content = f.read()
    return print(book_content)





main()