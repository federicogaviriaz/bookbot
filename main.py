from stats import count_words
from stats import count_chars
from stats import sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 main.py <path_to_book>")
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_chars(text)
    chars_sorted_list = sort_dictionary(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)
    
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

    

main()

