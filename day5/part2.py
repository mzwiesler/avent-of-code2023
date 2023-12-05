import portion as p

from part1 import get_final_mapping_table, read_data


def get_destination_interval(map, interval: p.interval.Interval) -> p.interval.Interval:
    start = map["destination_start"] + interval.lower - map["source_start"]
    end = start - interval.lower + interval.upper
    return p.closed(start, end)


def get_remainder(
    a: p.interval.Interval, b: p.interval.Interval
) -> p.interval.Interval:
    remainder = a - b
    remainder = remainder.apply(
        lambda x: x.replace(lower=lambda v: v + 1, left=p.CLOSED)
        if x.left == p.OPEN
        else x
    )
    remainder = remainder.apply(
        lambda x: x.replace(upper=lambda v: v - 1, right=p.CLOSED)
        if x.right == p.OPEN
        else x
    )
    return remainder


def get_intervalls(
    maps: list[dict], interval: p.interval.Interval
) -> list[p.interval.Interval]:
    target_intervals = []
    for map in maps:
        source_interval = p.closed(map["source_start"], map["source_end"])
        if source_interval.overlaps(interval):
            target_intervals.append(
                get_destination_interval(map, source_interval & interval)
            )
    source_interval = p.empty()
    for map in maps:
        source_interval = source_interval | p.closed(
            map["source_start"], map["source_end"]
        )
    remainder = get_remainder(interval, source_interval)
    if not remainder.empty:
        target_intervals.append(remainder)
    return target_intervals


def get_final_path(mapping_table: dict, interval: p.interval.Interval) -> list:
    target = "seed"
    path = []
    path.append(interval)
    while target != "location":
        new_target = mapping_table[target]["target"]
        new_path = []
        for item in path:
            intervals = get_intervalls(mapping_table[target]["maps"], item)
            new_path.extend(intervals)
        target = new_target
        path = new_path
    return path


def get_minimum(intervals: list[p.interval.Interval]) -> int:
    minimum = None
    for interval in intervals:
        if minimum is None:
            minimum = interval.lower
        else:
            if minimum > interval.lower:
                minimum = interval.lower
    return minimum


def main(file_path: str) -> int:
    parts = read_data(file_path)
    start_numbers = [
        int(number) for number in parts[0].split(":")[1].strip().split(" ")
    ]
    start_intervals = []
    for i in range(0, len(start_numbers), 2):
        start_intervals.append(
            p.closed(start_numbers[i], start_numbers[i] + start_numbers[i + 1] - 1)
        )
    final_mapping = get_final_mapping_table(parts)
    paths = []
    for interval in start_intervals:
        paths.extend(get_final_path(final_mapping, interval))
    min_number = get_minimum(paths)
    return min_number


if __name__ == "__main__":
    print(main("input.txt"))
