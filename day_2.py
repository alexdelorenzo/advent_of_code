def get_dim(dim_str: str) -> (int, int, int):
    return tuple(int(char) for char in dim_str.split('x'))


def get_surface_area(l: int, w: int, h: int) -> int:
    return 2*l*w + 2*w*h + 2*h*l


def get_lowest_pair(l: int, w: int, h: int) -> (int, int):
    return sorted((l, w, h))[:2]


def get_extra(l: int, w: int, h: int) -> int:
    low1, low2 = get_lowest_pair(l, w, h)

    return low1 * low2


def wrapping_paper(l: int, w: int, h: int) -> int:
    return get_surface_area(l, w, h) + get_extra(l, w, h)


def ribbon(l: int, w: int, h: int) -> int:
    a, b = get_lowest_pair(l, w, h)

    return 2*a + 2*b


def bow(l: int, w: int, h: int) -> int:
    return l * w * h


def total_ribbon(l: int, w: int, h: int) -> int:
    return ribbon(l, w, h) + bow(l, w, h)


def solve_p2(source: str):
    return sum(total_ribbon(*get_dim(line))
               for line in source.split("\n"))
