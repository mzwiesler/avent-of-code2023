from part1 import main


def test_main():
    assert main("example.txt", factor=2) == 374
