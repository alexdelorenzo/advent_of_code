from hashlib import md5
from itertools import count


MATCH = "00000"


def get_bytes(source: str) -> bytes:
    return bytes(source, 'utf-8')


def get_md5_hex(source: bytes) -> str:
    return md5(source).hexdigest()


def match_beginning(source: str, match: str=MATCH) -> bool:
    return source[:len(match)] == match


def is_matching_hash(source: str, num: int) -> bool:
    new_str = source + str(num)

    return match_beginning(get_md5_hex(get_bytes(new_str)))


def find_hash(source: str) -> int:
    for num in count():
        if is_matching_hash(source, num):
            return num
