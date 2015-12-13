BAD = {'i', 'o', 'l'}
LOW, HIGH = 'a', 'z'
MAX_CHARS = 8


def length_and_case(source: str):
    if len(source) != MAX_CHARS:
        return False

    return all(LOW <= char <= HIGH
               for char in source)


def contains_identical_pair(password: str, stop: int=2, count: int=0) -> bool:
    # want a laugh: print this out and show your friends
    if count == stop:
        return True

    length = len(password)

    for index in range(length - 1):
        end_index = index + 2

        x, y = password[index:end_index]

        if x == y:
            count += 1

            return contains_identical_pair(password[end_index:], count=count)

    return count == stop


def contains_bad(password: str) -> bool:
    return any(bad in password for bad in BAD)


def contains_straight(password: str, count: int=3) -> bool:
    length = len(password)

    for index in range(length - 1):
        end_index = index + 3
        x, y, z = map(ord, password[index:end_index])

        if y == x + 1 and z == x + 2:
            return True

    return False


def is_good_password(password: str) -> bool:
    return length_and_case(password) \
           and contains_identical_pair(password) \
           and not contains_bad(password) \
           and contains_straight(password)


def increment_password(password: str) -> str:
    last = password[-1]

    if last == 'z':
        return increment_password(password[:-1]) + 'a'

    return password[:-1] + chr(ord(last) + 1)


def find_good_password(password: str) -> str:
    while True:
        password = increment_password(password)

        if is_good_password(password):
            return password