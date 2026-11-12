from collections import defaultdict


def get_num_words(content: str) -> int:
    return len(content.split())


def get_word_frequency(content: str) -> defaultdict[str, int]:
    content = content.lower()

    data: defaultdict[str, int] = defaultdict(int)
    for word in content:  # content.split():
        data[word] += 1

    return data


def chars_dict_to_sorted_list(items: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(items.items(), key=lambda x: -x[1])
