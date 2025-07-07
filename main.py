from stats import count_words, number_of_each_character


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


def main():
    file_path = "books/frankenstein.txt"
    content = read_file(file_path)
    word_count = count_words(content)
    print(f"{word_count} words found in the document")
    char_count = number_of_each_character(content)
    print(f"Number of each character:\n{char_count}")


main()
