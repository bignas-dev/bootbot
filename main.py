from pathlib import Path

from stats import chars_dict_to_sorted_list, get_num_words, get_word_frequency


def get_book_text(file_path: Path) -> str:
    with open(file_path, "r") as f:
        return f.read()


def main():
    content = get_book_text(Path("./books/frankenstein.txt"))
    word_count = get_num_words(content)
    print(f"Found {word_count} total words")
    word_frequency = get_word_frequency(content)
    for item in chars_dict_to_sorted_list(word_frequency):
        print(item)


if __name__ == "__main__":
    main()
