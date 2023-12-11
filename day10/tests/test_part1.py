from part1 import main


def test_main():
    assert main("example.txt") == 4
    assert main("example1.txt") == 8
