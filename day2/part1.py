MAX_CUBES = {"red": 12, "green": 13, "blue": 14}


def valid_color_num(color: str, num: int) -> bool:
    if MAX_CUBES[color] >= num:
        return True
    return False


def split_id_game(line: str) -> tuple[int, str]:
    splitted_line = line.split(":")
    draws_raw = splitted_line[1]
    return int(splitted_line[0].split(" ")[1]), draws_raw


def convert_draw_to_dict(draw: str) -> dict[str, int]:
    draws_dict = {}
    rounds = draw.split(",")
    for round in rounds:
        cubes = round.strip().split(" ")
        draws_dict[cubes[1]] = int(cubes[0])
    return draws_dict


def get_valid_id(line: str) -> int:
    id, draws_raw = split_id_game(line)
    draws = draws_raw.split(";")
    for draw in draws:
        draw_dict = convert_draw_to_dict(draw)
        for color, num in draw_dict.items():
            if not valid_color_num(color, num):
                return 0
    return id


def main(file_path: str):
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    valid_ids = []
    for line in lines:
        valid_ids.append(get_valid_id(line))
    print(valid_ids)
    return sum(valid_ids)


if __name__ == "__main__":
    print(main("input.txt"))
