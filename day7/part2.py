from part1 import TYPE_STRENGTH, get_dict, get_hand, get_hand_strength

CARD_STRENGTH = {
    "2": "02",
    "3": "03",
    "4": "04",
    "5": "05",
    "6": "06",
    "7": "07",
    "8": "08",
    "9": "09",
    "T": "10",
    "J": "01",
    "Q": "11",
    "K": "12",
    "A": "13",
}


def get_type(hand: dict) -> str:
    num_j = hand.get("J", 0)
    if num_j == 5:
        return "Five of a kind"
    if "J" in hand:
        hand.pop("J")
    sorted_nums = sorted(hand.values(), reverse=True)
    sorted_nums[0] = sorted_nums[0] + num_j

    if sorted_nums[0] == 5:
        return "Five of a kind"
    if sorted_nums[0] == 1:
        return "High card"
    if sorted_nums[0] == 4:
        return "Four of a kind"
    if sorted_nums[0] == 3:
        if sorted_nums[1] == 2:
            return "Full house"
        return "Three of a kind"
    if sorted_nums[0] == 2:
        if sorted_nums[1] == 2:
            return "Two pair"
    return "One pair"


def main(file_path: str):
    # Read in the input file as string
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    hands = [get_hand(line, get_type=get_type, get_dict=get_dict) for line in lines]
    for hand in hands:
        hand["strength"] = get_hand_strength(hand, CARD_STRENGTH, TYPE_STRENGTH)
    hands.sort(key=lambda x: x["strength"], reverse=False)
    result = 0
    for i, hand in enumerate(hands):
        result += (i + 1) * int(hand["bid"])
    return result


if __name__ == "__main__":
    print(main("input.txt"))
