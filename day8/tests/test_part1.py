from part1 import main


def test_main():
    assert main("example1.txt") == 2
    assert main("example2.txt") == 6
