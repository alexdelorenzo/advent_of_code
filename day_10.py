from functools import lru_cache, partial
from types import GeneratorType


ITERATIONS = 40
ITERATIONS_P2 = 50


def gen_chunks(source: str):
    # this generator right here is shameful
    # should have used itertools.groupby()

    length = len(source)

    if length == 1:
        yield source[0]
        return

    current_chr = source[0]
    repeating_str = current_chr

    for index in range(1, length):
        letter = source[index]

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


def solve(source: str, iterations=ITERATIONS) -> int:
    return len(look_and_say(source))


solve_p2 = partial(solve, iterations=ITERATIONS_P2)