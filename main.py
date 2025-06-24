import sys
from stats import * 

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        book_content = get_book_text(sys.argv[1])
        book_dictionary = char_count(book_content)
        char_dict_list = sort_dict(book_dictionary)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {word_count(book_content)} total words")
        print("--------- Character Count -------")


        for dict_entry in char_dict_list:
            if dict_entry["char"].isalpha():
                print(f"{dict_entry["char"]}: {dict_entry["num"]}")

        print("============= END ===============")


main()
