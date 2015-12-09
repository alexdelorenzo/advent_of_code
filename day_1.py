vals = {'(': 1,
        ')': -1}

BASEMENT = -1
OFFSET = 1


def santa_floor(source: str) -> int:
    return sum(vals[char] for char in source)


def floor_position(source: str, floor_num: int=BASEMENT) -> int:
    total = 0

    for index, char in enumerate(source):
        total += vals[char]

        if total == floor_num:
            return index + OFFSET