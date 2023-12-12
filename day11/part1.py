from typing import Tuple


def parse(file_path: str) -> list[str]:
    # Read in the input file as string
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    return lines


def get_empty_lines(universe: list[str]) -> list[int]:
    empty_lines = []
    for i, line in enumerate(universe):
        if "#" not in line:
            empty_lines.append(i)
    empty_lines.sort()
    return empty_lines


def get_empty_columns(universe: list[str]) -> list[int]:
    empty_columns = []
    for i in range(len(universe[0])):
        column = "".join([line[i] for line in universe])
        if "#" not in column:
            empty_columns.append(i)
    empty_columns.sort()
    return empty_columns


def expand_universe(universe: list[str]) -> Tuple[list[int], list[int]]:
    this_universe = universe.copy()
    empty_lines = get_empty_lines(this_universe)
    empty_columns = get_empty_columns(this_universe)
    return (empty_lines, empty_columns)


def get_galaxies(universe: list[str]) -> list[Tuple[int, int]]:
    galaxies = []
    for i, line in enumerate(universe):
        for j, char in enumerate(line):
            if char == "#":
                galaxies.append((i, j))
    return galaxies


def get_difference(galaxy1: Tuple[int, int], galaxy2: Tuple[int, int]) -> int:
    distance = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    return distance


def get_empty_lines_between(
    galaxy1: Tuple[int, int], galaxy2: Tuple[int, int], empty_lines: list[int]
) -> int:
    lines_between = [line for line in empty_lines if galaxy1[0] < line < galaxy2[0]]
    return len(lines_between)


def get_empty_columns_between(
    galaxy1: Tuple[int, int], galaxy2: Tuple[int, int], empty_columns: list[int]
) -> int:
    columns_between = [
        column
        for column in empty_columns
        if min(galaxy1[1], galaxy2[1]) < column < max(galaxy1[1], galaxy2[1])
    ]
    return len(columns_between)


def get_differences(
    galaxies: list[Tuple[int, int]],
    empty_lines: list[int],
    empty_columns: list[int],
    factor: int,
) -> list[int]:
    differences = []
    for i, galaxy1 in enumerate(galaxies):
        for galaxy2 in galaxies[i + 1 :]:
            shortest_path = (
                get_difference(galaxy1, galaxy2)
                + get_empty_columns_between(galaxy1, galaxy2, empty_columns)
                * (factor - 1)
                + get_empty_lines_between(galaxy1, galaxy2, empty_lines) * (factor - 1)
            )
            differences.append(shortest_path)
    return differences


def main(file_path: str, factor: int) -> int:
    universe = parse(file_path)
    result = []
    empty_lines, empty_columns = expand_universe(universe)
    galaxies = get_galaxies(universe)
    result = get_differences(galaxies, empty_lines, empty_columns, factor)
    return sum(result)


if __name__ == "__main__":
    print(main("input.txt", factor=100))
