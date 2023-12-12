from part1 import main


def test_main():
    assert main("example.txt", factor=10) == 1030
    assert main("example.txt", factor=100) == 8410
