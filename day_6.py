from typing import Tuple
from re import compile


Point = Tuple[int, int]
RE_STR = "(?P<command>[a-z ]*)(?P<start>[0-9,]*) through (?P<end>[0-9,]*)"
RE_C = compile(RE_STR)


def parse_line(source: str) -> dict:
    match = RE_C.match(source)

    return match.groups()


def parse_lines(source: str, lights: list):
    for line in source.split("\n"):
        cmd = get_command_args(parse_line(line))
        apply(*cmd, lights)


def get_solution(source: str) -> int:
    lights = [[0 for x in range(1000)]
              for y in range(1000)]

    parse_lines(source, lights)

    return sum(y for x in lights for y in x)


def get_point(pt_str: str) -> Point:
    x, y = pt_str.split(',')

    return int(x), int(y)


def get_command_args(line: (str, str, str)) -> Tuple[str, Point, Point]:
    cmd, begin, end = line

    return cmd, get_point(begin), get_point(end)


def apply(command: str, begin: tuple, end: tuple, lights: list):
    for x in range(begin[0], end[0] + 1):
        for y in range(begin[1], end[1] + 1):
            COMMANDS[command](lights, x, y)


def turn_on(lights: list, x: int, y: int):
    lights[x][y] = 1


def turn_off(lights: list, x: int, y: int):
    lights[x][y] = 0


def toggle(lights: list, x: int, y: int):
    val = lights[x][y]
    lights[x][y] = 1 if val is 0 else 0


COMMANDS = {'turn on ': turn_on,
            'toggle ': toggle,
            'turn off ': turn_off}