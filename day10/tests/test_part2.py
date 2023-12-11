from part2 import main


def test_main():
    assert main("example2.txt") == 4
    assert main("example3.txt") == 8
    assert main("example4.txt") == 10
