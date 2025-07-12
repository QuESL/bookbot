def get_num_words(book_text):
    return len(book_text.split())

def get_num_characters(book_text):
    book_text = book_text.lower()
    counts = {}
    for character in book_text:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
    return counts
