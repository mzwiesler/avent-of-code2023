from part1 import get_own_numbers, get_own_winning_numbers, get_winning_numbers


def add_cards(cards: dict[int, int], num: int, card: int) -> dict[int, int]:
    if num == 0:
        return cards
    for n in range(card + 1, card + num + 1):
        cards[n] = cards.get(n, 0) + cards[card]
    return cards


def main(file_path: str):
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    cards = {}
    for i in range(1, len(lines) + 1):
        cards[i] = 1

    for i, line in enumerate(lines):
        winning_numbers = get_winning_numbers(line.split("|")[0])
        own_numbers = get_own_numbers(line.split("|")[1])
        own_winning_numbers = get_own_winning_numbers(winning_numbers, own_numbers)
        cards = add_cards(cards, len(own_winning_numbers), i + 1)

    return sum(list(cards.values()))


if __name__ == "__main__":
    print(main("input.txt"))
