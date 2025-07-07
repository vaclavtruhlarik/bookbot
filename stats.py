def count_words(content):
    """Count the number of words in a given string."""
    words = content.split()
    return len(words)


def number_of_each_character(content):
    """Count the number of each character in a given string."""
    char_count = {}
    for char in content.lower():
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count
