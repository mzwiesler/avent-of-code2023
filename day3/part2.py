import itertools
from functools import reduce

from part1 import get_position_number, get_symbols, is_symbol


def is_symbol(s: str) -> bool:
    if s == "*":
        return True
    else:
        return False


def get_adjacent_numbers(
    row: int, col: int, number_dict: dict[int, list[dict[str, int]]]
) -> list[int]:
    relevant_numbers_rows = [
        v for k, v in number_dict.items() if row - 1 <= k <= row + 1
    ]
    relevant_numbers_rows2 = list(itertools.chain(*relevant_numbers_rows))
    relevant_numbers = [
        number["number"]
        for number in relevant_numbers_rows2
        if any(
            num in range(col - 1, col + 2)
            for num in range(number["start"], number["end"] + 1)
        )
    ]
    return relevant_numbers


def main(file_path: str) -> int:
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    number_dict = {}
    symbol_dict = {}
    for i, line in enumerate(lines):
        symbol_dict[i] = get_symbols(line, is_symbol=is_symbol)
        extended_line = line + "."
        number_dict[i] = get_position_number(extended_line)
    result = []
    for row, v in symbol_dict.items():
        for col in v:
            adjacent_numbers = get_adjacent_numbers(
                row=row, col=col, number_dict=number_dict
            )
            if len(adjacent_numbers) == 2:
                result.append(reduce((lambda x, y: x * y), adjacent_numbers))
    return sum(result)


if __name__ == "__main__":
    print(main("input.txt"))
