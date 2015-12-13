from collections import defaultdict
from itertools import permutations
from typing import Dict


AdjMat = Dict[str, Dict[str, int]]


def get_adj_map(source: str) -> AdjMat:
    adj_mat = defaultdict(dict)

    for line in source.split('\n'):
        origin, dest, val = parse(line)
        adj_mat[origin][dest] = val

    return adj_mat


def solve(source: str) -> int:
    return find_permutation(get_adj_map(source))


def solve_pt2(source: str) -> int:
    adj_map = get_adj_map(source)

    for key, val in adj_map.copy().items():
        adj_map[key]["Me"] = 0
        adj_map["Me"][key] = 0

    return find_permutation(adj_map)


def parse(line: str) -> (str, str, int):
    begin_val_str, dest = line.split(" happiness units by sitting next to ")
    split_at = "gain " if "gain" in line else "lose "
    begin, val = begin_val_str.split(" would " + split_at)
    dest = dest[:-1]
    val = int(val) if "gain" in line else - int(val)

    return begin, dest, val


def calculate_happiness(people: tuple, adj_mat: AdjMat) -> int:
    total_happiness = 0

    for index in range(-1, len(people) - 1):
        begin, dest = people[index], people[index + 1]
        happiness = adj_mat[begin][dest] + adj_mat[dest][begin]
        total_happiness += happiness

    return total_happiness


def find_permutation(adj_mat: AdjMat):
    perms = permutations(adj_mat)
    perm = next(perms)
    high_happiness = calculate_happiness(perm, adj_mat)

    for perm in perms:
        happiness = calculate_happiness(perm, adj_mat)

        if happiness > high_happiness:
            high_happiness = happiness

    return high_happiness
