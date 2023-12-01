from part1 import calculate_sum, is_int

### Day 1 Puzzle part 2


VALID_CHARS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


# replace string with number
def replace_string_with_number(input: str) -> str:
    for key, value in VALID_CHARS.items():
        if key in input:
            return value
    return ""


# Get first digit of each line with checking for strings
def get_first_digit(line) -> str:
    for i, c in enumerate(line):
        number = replace_string_with_number(line[max(0, i - 5) : i + 1])
        if is_int(c):
            return c
        if is_int(number):
            return number
    raise ValueError("No digit found in line: " + line)


# Get last digit of each line with checking of strings
def get_last_digit(line) -> str:
    for i, c in reversed(list(enumerate(line))):
        number = replace_string_with_number(line[i : i + 5])
        if is_int(c):
            return c
        if is_int(number):
            return number
    raise ValueError("No digit found in line: " + line)


def main(file_path: str) -> int:
    # Read in the input file as string
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    print(lines)
    return calculate_sum(lines, get_first_digit, get_last_digit)


if __name__ == "__main__":
    print(main("input.txt"))
