from dataclasses import dataclass
from functools import reduce
from typing import Tuple

import numpy as np

FROM_TO = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E",
}
TILES = {
    "|": "NS",
    "-": "EW",
    "L": "EN",
    "7": "SW",
    "J": "NW",
    "F": "ES",
    "S": "NSWE",
    ".": "",
}

TRAVEL = {
    "N": np.array([-1, 0]),
    "S": np.array([1, 0]),
    "E": np.array([0, 1]),
    "W": np.array([0, -1]),
}


@dataclass
class Position:
    coordinate: Tuple[int, int]
    tile: str
    from_direction: str
    to_direction: str
    iteration: int


def parse(file_path: str) -> list[str]:
    # Read in the input file as string
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    return lines


def find_starting_directions(
    coordinates: Tuple[int, int], grid: list[list[str]]
) -> Tuple[str, str]:
    starting_directions = []
    for direction, coord in TRAVEL.items():
        new_coordinates = tuple(coordinates + coord)
        if any(np.array(new_coordinates) < 0):
            continue
        if FROM_TO[direction] in TILES[grid[new_coordinates[0]][new_coordinates[1]]]:
            starting_directions.append(direction)
    return tuple(starting_directions)


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


def gen_next_position(position: Position, grid: list[list[str]]):
    while 1:
        new_coordinates = tuple(position.coordinate + TRAVEL[position.to_direction])
        tile = grid[new_coordinates[0]][new_coordinates[1]]
        from_dir = FROM_TO[position.to_direction]
        position = Position(
            coordinate=new_coordinates,
            tile=tile,
            from_direction=from_dir,
            to_direction=TILES[tile].replace(from_dir, ""),
            iteration=position.iteration + 1,
        )
        yield position


def main(file_path: str) -> int:
    lines = parse(file_path)
    grid = [list(line) for line in lines]
    starting_position = find_starting_position(grid)
    starting_position_2 = Position(
        coordinate=starting_position.coordinate,
        tile=starting_position.tile,
        from_direction=starting_position.to_direction,
        to_direction=starting_position.from_direction,
        iteration=starting_position.iteration,
    )
    gens = [
        gen_next_position(starting_position, grid),
        gen_next_position(starting_position_2, grid),
    ]
    way = [next(gen) for gen in gens]
    i = 0
    while way[0].coordinate != way[1].coordinate:
        way[i % 2] = next(gens[i % 2])
        i += 1
    return max(way[0].iteration, way[1].iteration)


if __name__ == "__main__":
    print(main("input.txt"))
