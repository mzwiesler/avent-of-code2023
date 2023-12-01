### Day 1 Puzzle part 1


# Check if string can be converted to integer
from typing import Callable


def is_int(s) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


# Get first digit of each line omitting characters
def get_first_digit(line: str) -> str:
    for char in line:
        if is_int(char):
            return char
    raise ValueError("No digit found in line: " + line)


# Get last digit of each line omitting characters
def get_last_digit(line: str) -> str:
    for char in line[::-1]:
        if is_int(char):
            return char
    raise ValueError("No digit found in line: " + line)


def get_first_and_last_digit(
    line: str,
    get_first_digit: Callable[[str], str],
    get_last_digit: Callable[[str], str],
) -> str:
    first_digit = get_first_digit(line)
    last_digit = get_last_digit(line)
    return first_digit + last_digit


# determine sum
def calculate_sum(
    lines: list[str],
    get_first_digit: Callable[[str], str],
    get_last_digit: Callable[[str], str],
) -> int:
    # only keep first and last entry of each line as integer
    calibration = []
    for line in lines:
        calibration.append(
            int(get_first_and_last_digit(line, get_first_digit, get_last_digit))
        )

    # get sum
    result = sum(calibration)

    return result


def main(file_path: str) -> int:
    # Read in the input file as string
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line

    return calculate_sum(lines, get_first_digit, get_last_digit)


if __name__ == "__main__":
    print(main("input.txt"))
