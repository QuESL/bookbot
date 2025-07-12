from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_list_of_dict

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")

    word_count = get_num_words(book_text)
    # print(f"{word_count} words found in the document")

    character_count = get_num_characters(book_text)
    # for char, count in character_count.items():
    #     print(f"'{char}': {count}")

    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
    """)

    sorted_list_of_dict = get_sorted_list_of_dict(character_count)
    for item in sorted_list_of_dict:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")
    
main()