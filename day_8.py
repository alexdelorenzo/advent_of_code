from typing import Generator


## A day later: way to overcomplicate this problem

HEX_CHAR_LEN = 4


def parse_lines(source: str) -> Generator[str, None, None]:
    for line in source.split('\n'):
        yield parse_line(line)


def parse_line(line: str) -> int:
    line = replace_simple_escapes(line)
    line = find_replace_hex(line)

    return len(line)


def replace_simple_escapes(line: str) -> str:
    line = line.strip('"')
    line = line.replace('\"', '"')
    line = line.replace("\'", "'")
    line = line.replace("\\", "/") # let's not mess with further parsing

    return line


def hex_index(line: str, index: int=0) -> int:
    return line.find("\\x", index)


def find_replace_hex(line: str) -> str:
    index = 0
    length = len(line)
    h_index = hex_index(line, index)

    while h_index != -1:
        escaped_hex = line[h_index:HEX_CHAR_LEN]
        line.replace(escaped_hex, str(escaped_hex))
        h_index = hex_index(line, index)
        print(h_index)

    return line