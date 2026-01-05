#libs
from stats import num_words

def main():

    # books to read
    book_name = "books/frankenstein.txt"
    get_book_text(book_name)
    num_words(get_book_text(book_name))




def get_book_text(book_name):
    with open(book_name) as f:
        book_content = f.read()
    return book_content

main()