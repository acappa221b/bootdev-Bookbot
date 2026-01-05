def main():

    # books to read
    book_name = "books/frankenstein.txt"
    get_book_text(book_name)
    num_words(get_book_text(book_name))




def get_book_text(book_name):
    with open(book_name) as f:
        book_content = f.read()
    return book_content

def num_words(book):
    words = book.split()
    return print (f"Found {len(words)} total words")



main()