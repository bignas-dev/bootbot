from pathlib import Path


def get_book_text(file_path: Path) -> str:
    with open(file_path, "r") as f:
        return f.read()


def main():
    content = get_book_text(Path("./books/frankenstein.txt"))
    print(content)


if __name__ == "__main__":
    main()
