from collections import defaultdict


def group_anagram(words: list[str]) -> list[list[str]]:
    words = [word.lower() for word in words]
    anagrams = defaultdict(list)
    for word in words:
        words_sorted = tuple(sorted(word))
        anagrams[words_sorted].append(word)

    result: list[list] = sorted([v for v in anagrams.values()])
    return result


def main():
    words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat', 'lamp', 'Palm', 'Note', 'Tone', 'act', 'cat']
    print(group_anagram(words))


if __name__ == '__main__':
    main()
