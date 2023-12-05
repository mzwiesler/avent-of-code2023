from typing import Callable


def is_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_symbol(s: str) -> bool:
    if not is_int(s) and s != ".":
        return True
    else:
        return False


def get_symbols(line: str, is_symbol: Callable[[str], bool]) -> list[int]:
    symbol_list = []
    for i, c in enumerate(line):
        if is_symbol(c):
            symbol_list.append(i)
    return symbol_list


def get_position_number(line: str) -> list[dict[str, int]]:
    number_list = []
    beginning = None
    for i, c in enumerate(line):
        number_dict = {}
        if is_int(c) and beginning is None:
            beginning = i
        if not is_int(c):
            if beginning is not None:
                end = i
                number_dict["start"] = beginning
                number_dict["end"] = end - 1
                number_dict["number"] = int(line[beginning:end])
                number_list.append(number_dict)
            beginning = None
    return number_list


def check_if_symbol_is_adjacent(
    row: int, col_start: int, col_end: int, symbol_dict: dict[int, list[int]]
) -> bool:
    for i in range(row - 1, row + 2):
        if any(
            col_start - 1 <= symbol <= col_end + 1 for symbol in symbol_dict.get(i, [])
        ):
            return True
    return False


def main(file_path: str) -> int:
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    number_dict = {}
    symbol_dict = {}
    for i, line in enumerate(lines):
        symbol_dict[i] = get_symbols(line, is_symbol=is_symbol)
    result = []
    for i, line in enumerate(lines):
        extended_line = line + "."
        number_list = get_position_number(extended_line)
        for number_dict in number_list:
            if check_if_symbol_is_adjacent(
                col_start=number_dict["start"],
                col_end=number_dict["end"],
                row=i,
                symbol_dict=symbol_dict,
            ):
                result.append(number_dict["number"])
    return sum(result)


if __name__ == "__main__":
    print(main("input.txt"))
