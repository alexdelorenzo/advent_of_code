from functools import lru_cache, partial
from types import GeneratorType


ITERATIONS = 40
ITERATIONS_P2 = 50


def gen_chunks(input: str):
    # this generator right here is shameful
    # should have used itertools.groupby()

    length = len(input)

    if length == 1:
        yield input[0]
        return

    current_chr = input[0]
    repeating_str = current_chr

    for index in range(1, length):
        letter = input[index]

        if letter == current_chr:
            repeating_str += letter

        else:
            yield repeating_str
            repeating_str = letter

        current_chr = letter

    yield repeating_str


@lru_cache(maxsize=None)
def count_chunk(chunk: str):
    letter = chunk[0]
    length = len(chunk)

    return str(length) + letter


def parse_chunks(chunk_gen: GeneratorType) -> str:
    return ''.join(map(count_chunk, chunk_gen))


def look_and_say(start: str, iterations: int=ITERATIONS) -> str:
    string = start

    for _ in range(iterations - 1):
        string = parse_chunks(gen_chunks(string))

    return string


def solve(input: str, iterations=ITERATIONS) -> int:
    return len(look_and_say(input))


solve_p2 = partial(solve, iterations=ITERATIONS_P2)