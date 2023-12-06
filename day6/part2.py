from functools import reduce

from part1 import get_distance


def main(file_path: str):
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    time_str = lines[0].split(":")[1]
    distance_str = lines[1].split(":")[1]
    time = int(time_str.replace(" ", ""))
    distance = int(distance_str.replace(" ", ""))
    possible_push_times = []
    for push_time in range(1, time):
        race_distance = get_distance(push_time, time)
        if race_distance > distance:
            possible_push_times.append(push_time)
    result = len(possible_push_times)
    return result


if __name__ == "__main__":
    print(main("input.txt"))
