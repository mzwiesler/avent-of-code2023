def get_network_dict(network: list[str]) -> dict:
    """Get a dictionary of the network"""
    network_dict = {}
    for node in network:
        node_split = node.split(" = ")
        target = node_split[1].replace("(", "").replace(")", "").split(", ")
        network_dict[node_split[0]] = {}
        network_dict[node_split[0]]["L"] = target[0]
        network_dict[node_split[0]]["R"] = target[1]
    return network_dict


def parse(file_path: str) -> tuple[str, list[str]]:
    # Read in the input file as string
    with open(file_path, "r") as f:
        data = f.read()

    lines = data.split("\n")  # split by new line
    navigation = lines[0]
    network = lines[2:]
    return navigation, network


def execute_step(current: str, network_dict: dict, navigation: str) -> str:
    """Execute a step of the navigation"""
    return network_dict[current][navigation]


def main(file_path: str):
    navigation, network = parse(file_path)
    network_dict = get_network_dict(network)
    current = "AAA"
    i = 0
    while current != "ZZZ":
        nav = navigation[i % len(navigation)]
        current = execute_step(current, network_dict, nav)
        i += 1
    return i


if __name__ == "__main__":
    print(main("input.txt"))
