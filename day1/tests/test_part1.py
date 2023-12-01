from part1 import get_first_digit, get_last_digit, main


def test_get_first_digit():
    assert get_first_digit("two1nine") == "1"
    assert get_first_digit("r1twonqq") == "1"


def test_get_last_digit():
    assert get_last_digit("two1nine") == "1"
    assert get_last_digit("ghljgxzbfourcvqqntwo1r") == "1"


def test_main():
    assert main("example_part1.txt") == 142
