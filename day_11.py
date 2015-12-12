BAD = {'i', 'o', 'l'}
LOW, HIGH = ord('a'), ord('z')


def length_and_case(input: str):
    if len(input) != 8:
        return False

    return any(LOW <= ord(char) <= HIGH
               for char in input)


def contains_identical_pair(input: str, stop: int=2, count: int=0) -> bool:
    if count == stop:
        return True

    length = len(input)

    for index in range(length - 1):
        end_index = index + 2
        if end_index > length:
            break

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

        if end_index > length - 1:
            break

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


def replace_all_after_bad(input: str) -> str:
    # input = abciaaaa
    # output = abcjaaaa

    length = len(input)

    if contains_bad(input):
        for bad in BAD:
            index = input.find(bad)

            if index > -1:
                inc_chr = chr(ord(input[index]) + 1)
                filler = 'a' * (length - index - 1)
                input = input[:index] + inc_chr + filler

    return input


def find_good_password(input: str) -> str:
    password = input

    while True:
        password = replace_all_after_bad(increment_password(password))
        if is_good_password(password):
            return password