BAD = {'i', 'o', 'l'}
LOW, HIGH = 'a', 'z'
MAX_CHARS = 8


def length_and_case(input: str):
    if len(input) != MAX_CHARS:
        return False

    return all(LOW <= char <= HIGH
               for char in input)


def contains_identical_pair(input: str, stop: int=2, count: int=0) -> bool:
    # want a laugh: print this out and show your friends
    if count == stop:
        return True

    length = len(input)

    for index in range(length - 1):
        end_index = index + 2

        x, y = input[index:end_index]

        if x == y:
            count += 1

            return contains_identical_pair(input[end_index:], count=count)

    return count == stop


def contains_bad(input: str) -> bool:
    for bad in BAD:
        if bad in input:
            return True

    return False


def contains_straight(input: str, count: int=3) -> bool:
    length = len(input)

    for index in range(length - 1):
        end_index = index + 3
        x, y, z = map(ord, input[index:end_index])

        if y == x + 1 and z == x + 2:
            return True

    return False


def is_good_password(input: str) -> bool:
    return length_and_case(input) \
           and contains_identical_pair(input) \
           and not contains_bad(input) \
           and contains_straight(input)


def increment_password(input: str) -> str:
    last = input[-1]

    if last == 'z':
        return increment_password(input[:-1]) + 'a'

    return input[:-1] + chr(ord(last) + 1)


def find_good_password(password: str) -> str:
    while True:
        password = increment_password(password)

        if is_good_password(password):
            return password