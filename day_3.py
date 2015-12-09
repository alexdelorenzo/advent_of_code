from typing import Tuple, Dict


PointType = Tuple[int, int]
PresentMap = Dict[PointType, int]

directions = {'>': (1, 0),
              '^': (0, 1),
              '<': (-1, 0),
              'v': (0, -1)}


def move(direction: chr, starting_pt: PointType) -> PointType:
    start_x, start_y = starting_pt
    delta_x, delta_y = directions[direction]
    new_pt = start_x + delta_x, start_y + delta_y

    return new_pt


def parse_directions(direction_str: str, present_map: PresentMap):
    santa_pt = (0, 0)
    present_map[santa_pt] += 1

    for direction in direction_str:
        santa_pt = move(direction, santa_pt)
        present_map[santa_pt] += 1


def get_visits(present_map: PresentMap) -> int:
    return sum(1 for val in present_map.values() if val >= 1)


def get_robo_visits(source: str, present_map):
    even = source[::2]
    odd = source[1::2]

    parse_directions(even, present_map)
    parse_directions(odd, present_map)
