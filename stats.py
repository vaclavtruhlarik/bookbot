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


def sort_on(items, key="num"):
    """Helper function to sort a list of dictionaries by a specific key."""
    return items[key]


def sort_characters(char_count):
    """Sort the character count dictionary by number of use."""
    # From dictionary {"b": 2, "a": 1} to list of dictionaries [{"char": "b", "num": 2}, {"char": "a", "num": 1}]
    sorted_items = [{"char": char, "num": count} for char, count in char_count.items()]
    sorted_items.sort(reverse=True, key=sort_on)
    return sorted_items
