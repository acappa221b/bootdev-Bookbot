#libs
from stats import *
import sys

def main():

    # books to read
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_name = sys.argv[1]
    book = get_book_text(book_name)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    print("----------- Word Count ----------")
    num_words(book)
    print("--------- Character Count -------")
    print_letters(sort_letters(num_each_letter(book)))
    print("============ THE END ============")

main()