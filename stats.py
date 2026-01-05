def num_words(book):
    words = book.split()
    return print (f"Found {len(words)} total words")

def num_each_letter(book):
    letters = [char for char in book.lower() if char.isalpha()]
    unique_letters = set(letters)
    letter_count = {letter: letters.count(letter) for letter in unique_letters}
    return letter_count
