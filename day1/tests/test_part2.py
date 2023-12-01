from part2 import get_first_digit, get_last_digit, main


def test_get_first_digit():
    assert get_first_digit("two1nine") == "2"
    assert get_first_digit("r1twonqq") == "1"


def test_get_last_digit():
    assert get_last_digit("two1nine") == "9"
    assert get_last_digit("ghljgxzbfourcvqqntwo1r") == "1"


def test_main():
    assert main("example_part2.txt") == 281
