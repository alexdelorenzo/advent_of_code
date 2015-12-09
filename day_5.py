from collections import Counter


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
NAUGHTY_STRS = "ab", "cd", "pq", "xy"


def contains_vowels(source: str, min_vowels: int=3) -> bool:
    letter_count = Counter(source)
    vowel_count = sum(letter_count[vowel] for vowel in VOWELS)

    return vowel_count >= min_vowels


def contains_duplicate_letter(source: str) -> bool:
    return any(letter * 2 in source[index:]
               for index, letter in enumerate(source))


def contains_naughty_str(source: str) -> bool:
    return any(naughty_str in source
               for naughty_str in NAUGHTY_STRS)


def is_nice(source: str) -> bool:
    return contains_vowels(source) \
           and contains_duplicate_letter(source) \
           and not contains_naughty_str(source)


def count_nice_strs(sources: str) -> int:
    return sum(1 for source in sources.split() if is_nice(source))
