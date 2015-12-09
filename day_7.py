from collections import namedtuple
from operator import and_, lshift, rshift, or_


class OP(namedtuple("OP", 'op args')):
    def apply(self):
        return self.op(*self.args)


BITS = 16
OPS = {'AND': and_,
       'NOT': lambda x: ~x + 2**BITS,
       'LSHIFT': lshift,
       'RSHIFT': rshift,
       'OR': or_}


def parse_line(source: str, state: dict):
    value, name = source.split(' -> ')
    value = evaluate(value, state)

    state[name] = value


def parse_lines(source: str, state: dict):
    for line in source.split("\n"):
        parse_line(line, state)


def look_up(name: str, state: dict) -> int:
    name = name.strip()

    if name in state:
        return state[name]

    elif name.isdigit():
        return int(name)

    return name


def evaluate(value_str: str, state: dict) -> int:
    for op, func in OPS.items():
        if op in value_str:
            split_val = [val for val in value_str.split(op) if val]

            if len(split_val) == 2:
                operands = x, y = map(lambda x: look_up(x, state), split_val)

            elif len(split_val) == 1:
                operands = [look_up(split_val[0], state)]

            return OP(op, operands)

    return int(value_str.strip())