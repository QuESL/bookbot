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

def get_sorted_list_of_dict(character_dictionary):
    list_of_dict = list()
    for key, value in character_dictionary.items():
        new_sub_dict = {"char": key, "num": value}
        list_of_dict.append(new_sub_dict)
    list_of_dict.sort(reverse=True, key=lambda x: x["num"])
    return list_of_dict

