from stats import get_num_words
from stats import get_num_characters

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")

    word_count = get_num_words(book_text)
    print(f"{word_count} words found in the document")

    character_count = get_num_characters(book_text)
    for char, count in character_count.items():
        print(f"'{char}': {count}")

main()
