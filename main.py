from collections import defaultdict


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    char_counts = get_character_count(text)

    print_report(num_words, char_counts)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_character_count(text):
    char_count = defaultdict(int)
    for char in text.lower():
        char_count[char] += 1
    return char_count


def print_report(num_words, char_counts):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    char_counts_list = list(char_counts.items())
    char_counts_list.sort(key=lambda x: x[1], reverse=True)
    for char, value in char_counts_list:
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {value} times")
    print("--- End report ---")


main()
