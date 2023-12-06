from functools import reduce


def get_distance(push_time: int, race_time: int) -> int:
    if push_time >= race_time:
        return 0
    speed = push_time
    travel_time = race_time - push_time
    distance = speed * travel_time
    return distance


def main(file_path: str):
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    time_str = lines[0].split(":")[1]
    distance_str = lines[1].split(":")[1]
    times = [int(time.strip()) for time in time_str.split(" ") if time.strip() != ""]
    distances = [
        int(distance.strip())
        for distance in distance_str.split(" ")
        if distance.strip() != ""
    ]
    result = []
    for i, time in enumerate(times):
        possible_push_times = []
        for push_time in range(1, time):
            race_distance = get_distance(push_time, time)
            if race_distance > distances[i]:
                possible_push_times.append(push_time)
        result.append(len(possible_push_times))
    return reduce(lambda x, y: x * y, result)


if __name__ == "__main__":
    print(main("input.txt"))
