from typing import Callable

TYPE_STRENGTH = {
    "High card": "1",
    "One pair": "2",
    "Two pair": "3",
    "Three of a kind": "4",
    "Full house": "5",
    "Four of a kind": "6",
    "Five of a kind": "7",
}
CARD_STRENGTH = {
    "2": "01",
    "3": "02",
    "4": "03",
    "5": "04",
    "6": "05",
    "7": "06",
    "8": "07",
    "9": "08",
    "T": "09",
    "J": "10",
    "Q": "11",
    "K": "12",
    "A": "13",
}


def get_hand_strength(hand: dict, card_strength: dict, type_strength: dict) -> int:
    strength = type_strength[hand["type"]]
    for card in hand["cards"]:
        strength += card_strength[card]
    return int(strength)


def get_type(hand: dict) -> str:
    if len(hand) == 5:
        return "High card"
    if len(hand) == 4:
        return "One pair"
    if len(hand) == 3:
        if 3 in hand.values():
            return "Three of a kind"
        return "Two pair"
    if len(hand) == 2:
        if 4 in hand.values():
            return "Four of a kind"
        return "Full house"
    return "Five of a kind"


def get_dict(hand: str):
    hand_dict = {}
    for card in hand:
        if card in hand_dict:
            hand_dict[card[0]] += 1
        else:
            hand_dict[card[0]] = 1
    return hand_dict


def compare_hands(
    hand1: dict, hand2: dict, type_strength: dict, card_strength: dict
) -> bool:
    if type_strength[hand1["type"]] > type_strength[hand2["type"]]:
        return True
    if type_strength[hand1["type"]] < type_strength[hand2["type"]]:
        return False
    for i, card in enumerate(hand1["cards"]):
        if card_strength[card] > card_strength[hand2["cards"][i]]:
            return True
        if card_strength[card] < card_strength[hand2["cards"][i]]:
            return False
    raise


def get_hand(line: str, get_type: Callable, get_dict: Callable) -> dict:
    cards = line.split(" ")[0]
    bid = line.split(" ")[1]
    hand = {}
    hand["cards"] = cards
    hand["bid"] = bid
    hand["type"] = get_type(get_dict(cards))
    return hand


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
