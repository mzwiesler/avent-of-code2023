def create_map(input: str) -> dict:
    map = {}
    values = input.strip().split(" ")
    if len(values) != 3:
        raise ValueError("Invalid input")
    map["destination_start"] = int(values[0])
    map["destination_end"] = map["destination_start"] + int(values[2])
    map["source_start"] = int(values[1])
    map["source_end"] = map["source_start"] + int(values[2])
    return map


def get_next_number(maps: list[dict], number: int) -> int:
    for map in maps:
        if number >= map["source_start"] and number < map["source_end"]:
            return map["destination_start"] + number - map["source_start"]
    return number


# def create_mapping_table_from_map(map: dict) -> dict:
#     mapping_table = {}
#     if map["length"] == 0:
#         return mapping_table
#     for i in range(map["length"]):
#         mapping_table[map["source_start"] + i] = map["destination_start"] + i
#     return mapping_table


# def create_mapping_table_from_maps(maps: list[dict]) -> dict:
#     mapping_tables = []
#     for i in range(len(maps)):
#         mapping_tables.append(create_mapping_table_from_map(maps[i]))
#     mapping_table = {k: v for table in mapping_tables for k, v in table.items()}
#     return mapping_table


def create_finale_mapping_table(part: str):
    target = part.split("-")[2].split(" ")[0]
    maps = []
    for line in part.split("\n")[1:]:
        maps.append(create_map(line))
    mapping = {}
    mapping["target"] = target
    mapping["maps"] = maps
    return mapping


def get_final_path(mapping_table: dict, start: int) -> list:
    target = "seed"
    path = []
    next_num = start
    path.append({"number": next_num})
    while target != "location":
        new_target = mapping_table[target]["target"]
        new_path = []
        for item in path:
            next_num = get_next_number(mapping_table[target]["maps"], item["number"])
            new_path.append({"number": next_num})
        target = new_target
        path = new_path
    return path


def read_data(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        data = f.read()
    parts = data.split("\n\n")  # split by new line
    return parts


def get_final_mapping_table(parts: list[str]) -> dict:
    final_mapping = {}
    for part in parts[1:]:
        origin = part.split("-")[0]
        final_mapping[origin] = create_finale_mapping_table(part)
    return final_mapping


def main(file_path: str) -> int:
    parts = read_data(file_path)
    start_numbers = [
        int(number) for number in parts[0].split(":")[1].strip().split(" ")
    ]
    final_mapping = get_final_mapping_table(parts)
    paths = []
    for number in start_numbers:
        paths.append(get_final_path(final_mapping, number))
    min_number = min([item["number"] for path in paths for item in path])
    return min_number


if __name__ == "__main__":
    print(main("input.txt"))
