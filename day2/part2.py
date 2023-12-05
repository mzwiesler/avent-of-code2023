import numpy as np

from part1 import convert_draw_to_dict, split_id_game


def get_minumum_cubes(line: str) -> dict[str, int]:
    _, draws_raw = split_id_game(line)
    draws = draws_raw.split(";")
    min_cubes = {}
    for draw in draws:
        draw_dict = convert_draw_to_dict(draw)
        for color, num in draw_dict.items():
            if min_cubes.get(color, 0) < num:
                min_cubes[color] = num
    return min_cubes


def main(file_path: str):
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    powers = []
    for line in lines:
        powers.append(np.prod(list(get_minumum_cubes(line).values())))
    return sum(powers)


if __name__ == "__main__":
    print(main("input.txt"))
