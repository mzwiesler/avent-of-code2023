from part1 import (
    main,
)  # , get_final_mapping_table, get_next_number, get_path, read_data


def test_main():
    assert main("example.txt") == 35


# def test_next_number():
#     maps = [
#         {"destination_start": 5, "source_start": 0, "length": 10},
#         {"destination_start": 20, "source_start": 30, "length": 10},
#     ]
#     assert get_next_number(maps, 0) == 5
#     assert get_next_number(maps, 9) == 14
#     assert get_next_number(maps, 15) == 15
#     assert get_next_number(maps, 35) == 25


# def test_path():
#     parts = read_data("example_part1.txt")
#     final_mapping = get_final_mapping_table(parts)
#     assert get_path(final_mapping, 79) == {
#         "seed": 79,
#         "soil": 81,
#         "fertilizer": 81,
#         "water": 81,
#         "light": 74,
#         "temperature": 78,
#         "humidity": 78,
#         "location": 82,
#     }
#     assert get_path(final_mapping, 14) == {
#         "seed": 14,
#         "soil": 14,
#         "fertilizer": 53,
#         "water": 49,
#         "light": 42,
#         "temperature": 42,
#         "humidity": 43,
#         "location": 43,
#     }
#     assert get_path(final_mapping, 55) == {
#         "seed": 55,
#         "soil": 57,
#         "fertilizer": 57,
#         "water": 53,
#         "light": 46,
#         "temperature": 82,
#         "humidity": 82,
#         "location": 86,
#     }
#     assert get_path(final_mapping, 13) == {
#         "seed": 13,
#         "soil": 13,
#         "fertilizer": 52,
#         "water": 41,
#         "light": 34,
#         "temperature": 34,
#         "humidity": 35,
#         "location": 35,
#     }
