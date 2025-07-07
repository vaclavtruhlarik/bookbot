from stats import count_words, number_of_each_character, sort_characters
import sys


def read_file(file_path):
    """Read the content of a file and return it as a string."""
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"


def print_characters(char_count):
    """Print the character count in a formatted way."""
    sorted_items = sort_characters(char_count)
    for item in sorted_items:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")


def print_report(book_name, word_count, char_count):
    """Print a report of the word and character counts."""
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_characters(char_count)
    print("============= END ===============")


def read_argvs():
    """Read command line arguments and return the file path."""
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]


def main():
    file_path = read_argvs()
    content = read_file(file_path)
    word_count = count_words(content)
    char_count = number_of_each_character(content)
    print_report(file_path, word_count, char_count)


main()
