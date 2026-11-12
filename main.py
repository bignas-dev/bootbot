from pathlib import Path


def get_text_len(content: str) -> int:
    return len(content.split())


def get_book_text(file_path: Path) -> str:
    with open(file_path, "r") as f:
        return f.read()


def main():
    content = get_book_text(Path("./books/frankenstein.txt"))
    word_count = get_text_len(content)
    print(f"Found {word_count} total words")


if __name__ == "__main__":
    main()
