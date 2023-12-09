from typing import Callable, Generator, Tuple


def parse(file_path: str) -> list[str]:
    # Read in the input file as string
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    return lines


def get_diff_generator(current_list: list[int], position: int):
    while 1:
        current_list = [
            current_list[i + 1] - current_list[i] for i in range(len(current_list) - 1)
        ]
        yield sum([abs(item) for item in current_list]), current_list[position]


def extrapolate(tree: list[int], position: int) -> int:
    factor = 1
    if position == 0:
        factor = -1
    next_number = 0
    for i in range(len(tree), 0, -1):
        next_number = tree[i - 1] + factor * next_number
    return next_number


def main(file_path: str, position: int) -> int:
    lines = parse(file_path)
    result = []
    for line in lines:
        tree = []
        sequence = line.split(" ")
        sequence = [int(item) for item in sequence]
        tree.append(sequence[position])
        gen = get_diff_generator(sequence, position)
        abs_sum, number = next(gen)
        while abs_sum > 0:
            tree.append(number)
            abs_sum, number = next(gen)
        result.append(extrapolate(tree, position))
    return sum(result)


if __name__ == "__main__":
    print(main("input.txt", -1))
