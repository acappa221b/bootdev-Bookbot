def num_words(book):
    words = book.split()
    return print (f"Found {len(words)} total words")

def num_each_letter(book):
    letters = [char for char in book.lower() if char.isalpha()]
    unique_letters = set(letters)
    letter_count = {letter: letters.count(letter) for letter in unique_letters}
    return letter_count

def sort_letters(letter_count):
    letters_count = list(letter_count.items())
    letters_count.sort(reverse=True, key=lambda x: x[1])
    return letters_count

def print_letters(letters_count):
    for letter, count in letters_count:
        print(f"{letter}: {count}")

def get_book_text(book_name):
    with open(book_name) as f:
        book_content = f.read()
    return book_content