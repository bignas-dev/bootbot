from pathlib import Path

from stats import get_num_words


def get_book_text(file_path: Path) -> str:
    with open(file_path, "r") as f:
        return f.read()


def main():
    content = get_book_text(Path("./books/frankenstein.txt"))
    word_count = get_num_words(content)
    print(f"Found {word_count} total words")


if __name__ == "__main__":
    main()
