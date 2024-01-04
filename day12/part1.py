from typing import Tuple


def parse(file_path: str) -> list[str]:
    # Read in the input file as string
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    return lines


def expand_input(record: str, conditions: list, factor: int) -> Tuple[str, list]:
    record = "?".join(factor * [record])
    conditions = factor * conditions
    return record, conditions


def split_line(line: str) -> Tuple[str, list[int]]:
    record = line.split(" ")[0]
    conditions = [int(condition) for condition in line.split(" ")[1].split(",")]
    while ".." in record:
        record = record.replace("..", ".")
    return record, conditions


def split_record(record: str) -> list[str]:
    if record[0] == ".":
        record = record[1:]
    if record[-1] == ".":
        record = record[:-1]
    return record.split(".")


def execute_step(record: list[str], conditions: list[int], cache: dict) -> int:
    key = "|".join(map(str, conditions))
    key += ":".join(record)
    if key in cache:
        return cache[key]

    if conditions == []:
        if any(["#" in cluster for cluster in record]):
            return 0
        return 1
    if record == []:
        return 0
    ret = 0

    ## start with first condition and record
    cluster = record[0]
    condition = conditions[0]
    len_cluster = len(cluster)
    if condition > len_cluster and "#" in cluster:
        return 0
    for i in range(len_cluster - condition + 1):
        left = cluster[:i]
        right = cluster[i + condition :]
        if not check_if_possible(left):
            break
        if right.startswith("#"):
            continue
        new_record = record[1:]
        if len(right) > 1:
            new_record.insert(0, right[1:])
        ret += execute_step(new_record, conditions[1:], cache)

    if "#" not in cluster:
        ret += execute_step(record[1:], conditions, cache)

    cache[key] = ret

    return ret


def check_if_possible(left: str) -> bool:
    if "#" in left:
        return False
    return True


def main(file_path: str, factor: int) -> int:
    records = parse(file_path)
    result = []
    for line in records:
        record_init, condition_init = split_line(line)
        record, condition = expand_input(record_init, condition_init, factor)
        record = split_record(record)
        result.append(execute_step(record, condition, {}))
    return sum(result)


if __name__ == "__main__":
    print(main("input.txt", 1))
