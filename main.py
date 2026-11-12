import sys
from pathlib import Path

from stats import chars_dict_to_sorted_list, get_num_words, get_word_frequency


def print_report(
    book_path: Path, word_count: int, char_frequency: list[tuple[str, int]]
):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}..")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in char_frequency:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")

    print("============= END ===============")


def get_book_text(file_path: Path) -> str:
    with open(file_path, "r") as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    content = get_book_text(file_path)
    word_count = get_num_words(content)
    word_frequency = get_word_frequency(content)
    sorted_list = chars_dict_to_sorted_list(word_frequency)
    print_report(file_path, word_count, sorted_list)


if __name__ == "__main__":
    main()
