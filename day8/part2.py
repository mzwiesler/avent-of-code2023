import math
from functools import reduce

from part1 import execute_step, get_network_dict, parse


def get_loop(
    current: str, network_dict: dict, navigation: str
) -> list[tuple[str, int]]:
    i = 0
    next_step = current
    position = (next_step, i)
    loop = []
    while position not in loop:
        loop.append(position)
        next_step = execute_step(next_step, network_dict, navigation[i])
        i = (i + 1) % len(navigation)
        position = (next_step, i)
    loop.append(position)
    return loop


def get_endpoint_positions_from_loop(loop: list[tuple[str, int]]) -> list[int]:
    endpoints = []
    for i in range(len(loop)):
        if loop[i][0][2] == "Z":
            endpoints.append(i)
    return endpoints


def get_loop_start(loop: list[tuple[str, int]]) -> int:
    end_position = loop[-1]
    for i in range(len(loop)):
        if loop[i] == end_position:
            return i
    raise ValueError("End position not found in loop")


def get_factors(loop: list[tuple[str, int]]) -> dict:
    factor = {}
    factor["start"] = get_loop_start(loop)
    factor["endpoints"] = get_endpoint_positions_from_loop(loop)
    factor["length"] = len(loop) - factor["start"] - 1
    return factor


def main(file_path: str):
    navigation, network = parse(file_path)
    network_dict = get_network_dict(network)
    current = [str(key) for key in network_dict.keys() if key[2] == "A"]
    factors = []
    for c in current:
        loop = get_loop(c, network_dict, navigation)
        factor = get_factors(loop)
        factors.append(factor)
    print(factors)
    min = math.lcm(*[factor["length"] for factor in factors])
    return min


if __name__ == "__main__":
    print(main("input.txt"))
