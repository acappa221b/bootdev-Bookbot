#libs
from stats import *
import sys

def main():

    # books to read
    if len(sys.argv) > 1:
        book_name = sys.argv[1]
    else:
        book_name = "books/frankenstein.txt"
    book = get_book_text(book_name)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    print("----------- Word Count ----------")
    num_words(book)
    print("--------- Character Count -------")
    print_letters(sort_letters(num_each_letter(book)))
    print("============ THE END ============")

main()