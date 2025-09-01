def count_words(text):
    num_words = text.split()
    return f"Found {len(num_words)} total words"

def count_chars(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_dictionary(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append ({"char":char, "num": char_dict[char]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

def sort_on(char_dict):
    return char_dict["num"]
    