from functools import reduce
from typing import Tuple

import numpy as np

from part1 import (
    FROM_TO,
    TILES,
    TRAVEL,
    Position,
    find_starting_directions,
    gen_next_position,
    parse,
)


def find_starting_position(grid: list[list[str]]) -> Position:
    for j, row in enumerate(grid):
        for i, element in enumerate(row):
            if element == "S":
                starting_directions = find_starting_directions((j, i), grid)
                list_start_dir = list(starting_directions)
                list_start_dir.sort()
                new_tile = [
                    key
                    for key, value in TILES.items()
                    if value == reduce(lambda i, j: i + j, list_start_dir)
                ][0]
                return Position(
                    coordinate=(j, i),
                    tile=new_tile,
                    from_direction=TILES[new_tile][0],
                    to_direction=TILES[new_tile][1],
                    iteration=0,
                )
    raise ValueError("No starting position found")


def get_num_internal(path: list[Position]):
    if len(path) < 2:
        return 0
    pos_dict = {}
    for pos in path:
        pos_dict[pos.coordinate[1]] = pos.to_direction + pos.from_direction
    keys = list(pos_dict.keys())
    keys.sort()
    start = None
    counted = False
    result = 0
    relevant_directions = ["NS", "SN"]
    not_relevant_directions = ["SS", "NN"]
    direction = ""
    for key in keys:
        current_direction = pos_dict[key].replace("W", "").replace("E", "")
        direction = direction + current_direction
        if start is not None:
            if ("S" in direction or "N" in direction) and counted is False:
                result += key - start - 1
                counted = True
            if direction in relevant_directions:
                start = None
            if direction in not_relevant_directions:
                start = key
        else:
            if direction in relevant_directions:
                start = key
        if direction in not_relevant_directions or direction in relevant_directions:
            direction = ""
            counted = False
    return result


def main(file_path: str) -> int:
    lines = parse(file_path)
    grid = [list(line) for line in lines]
    starting_position = find_starting_position(grid)
    path = [starting_position]
    gen = gen_next_position(starting_position, grid)
    next_point = next(gen)
    while next_point.tile != "S":
        path.append(next_point)
        next_point = next(gen)
    result = 0
    for row in range(1, len(grid)):
        result += get_num_internal([pos for pos in path if pos.coordinate[0] == row])
    return result


if __name__ == "__main__":
    print(main("input.txt"))
