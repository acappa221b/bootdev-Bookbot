#libs
from stats import *

def main():

    # books to read
    book_name = "books/frankenstein.txt"
    book = get_book_text(book_name)
    num_words(book)
    print(num_each_letter(book))




def get_book_text(book_name):
    with open(book_name) as f:
        book_content = f.read()
    return book_content

main()