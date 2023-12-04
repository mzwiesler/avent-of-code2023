def get_winning_numbers(line: str) -> list[int]:
    numbers_str = line.split(":")[1]
    numbers_list = numbers_str.split(" ")
    numbers = [int(num.strip()) for num in numbers_list if num.strip() != ""]
    return numbers


def get_own_numbers(line: str) -> list[int]:
    numbers_list = line.split(" ")
    numbers = [int(num.strip()) for num in numbers_list if num.strip() != ""]
    return numbers


def get_own_winning_numbers(win_nums: list[int], own_nums: list[int]) -> list[int]:
    own_winning_numbers = []
    for num in own_nums:
        if num in win_nums:
            own_winning_numbers.append(num)
    return own_winning_numbers


def main(file_path: str):
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    result = []
    for line in lines:
        winning_numbers = get_winning_numbers(line.split("|")[0])
        own_numbers = get_own_numbers(line.split("|")[1])
        own_winning_numbers = get_own_winning_numbers(winning_numbers, own_numbers)
        if len(own_winning_numbers) > 0:
            result.append(2 ** (len(own_winning_numbers) - 1))
    return sum(result)


if __name__ == "__main__":
    print(main("input.txt"))
