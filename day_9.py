from collections import defaultdict
from functools import partial
from types import FunctionType
from typing import Generator, Tuple, Dict, Iterable
from itertools import permutations
from operator import gt, lt


SOURCE = """Faerun to Tristram = 65
Faerun to Tambi = 129
Faerun to Norrath = 144
Faerun to Snowdin = 71
Faerun to Straylight = 137
Faerun to AlphaCentauri = 3
Faerun to Arbre = 149
Tristram to Tambi = 63
Tristram to Norrath = 4
Tristram to Snowdin = 105
Tristram to Straylight = 125
Tristram to AlphaCentauri = 55
Tristram to Arbre = 14
Tambi to Norrath = 68
Tambi to Snowdin = 52
Tambi to Straylight = 65
Tambi to AlphaCentauri = 22
Tambi to Arbre = 143
Norrath to Snowdin = 8
Norrath to Straylight = 23
Norrath to AlphaCentauri = 136
Norrath to Arbre = 115
Snowdin to Straylight = 101
Snowdin to AlphaCentauri = 84
Snowdin to Arbre = 96
Straylight to AlphaCentauri = 107
Straylight to Arbre = 14
AlphaCentauri to Arbre = 46"""


LineType = Tuple[str, str, int]
LineGen = Generator[LineType, None, None]
AdjMat = Dict[str, Dict[str, int]]


def gen_lines(source: str=SOURCE) -> LineGen:
    for line in source.split("\n"):
        begin, dest, dist = line.split()[::2]

        yield begin, dest, int(dist)


def make_adj_matrix(lines: LineGen) -> AdjMat:
    adj_mat = defaultdict(dict)

    for begin, dest, dist in lines:
        adj_mat[begin][dest] = dist
        adj_mat[dest][begin] = dist

    return adj_mat


def calculate_dist(cities: tuple, adj_mat: AdjMat) -> int:
    total_dist = 0

    for index in range(0, len(cities) - 1):
        begin, dest = cities[index], cities[index + 1]
        dist = adj_mat[begin][dest]
        total_dist += dist

    return total_dist


def find_permutation(adj_mat: AdjMat, op: FunctionType=lt) -> Tuple[Iterable[str], int]:
    perms = permutations(adj_mat)
    short_perm = next(perms)
    short_dist = calculate_dist(short_perm, adj_mat)

    for cities in perms:
        dist = calculate_dist(cities, adj_mat)

        if op(dist, short_dist):
            short_dist = dist
            short_perm = cities

    return short_perm, short_dist


# pt 2
greatest_permutation = partial(find_permutation, op=gt)
