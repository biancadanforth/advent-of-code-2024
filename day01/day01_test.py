import pytest

from day01 import Puzzle


class TestPuzzle(object):
    def test_parse_input_well_formed(self):
        puzzle_input = "3   4\n4   3\n"
        expected = ([3, 4], [4, 3])
        assert Puzzle.parse_input(puzzle_input) == expected

    def test_parse_input_ignore_extra_chars(self):
        puzzle_input = "a3 b  4\n4   c3\n"
        expected = ([3, 4], [4, 3])
        assert Puzzle.parse_input(puzzle_input) == expected

    def test_parse_input_double_plus_digits(self):
        puzzle_input = "33   444\n44   3333\n"
        expected = ([33, 44], [444, 3333])
        assert Puzzle.parse_input(puzzle_input) == expected

    def test_parse_input_more_than_two_sets_of_numbers_per_line(self):
        # Takes the first two sets rather than throwing an error.
        puzzle_input = "3   4   5\n4   3\n"
        expected = ([3, 4], [4, 3])
        assert Puzzle.parse_input(puzzle_input) == expected

    def test_parse_input_one_set_of_numbers_per_line(self):
        puzzle_input = "3   4\ns   3\n"
        with pytest.raises(ValueError):
            Puzzle.parse_input(puzzle_input)

    def test_parse_input_no_sets_of_numbers_per_line(self):
        puzzle_input = "3   4\ns   a\n"
        with pytest.raises(ValueError):
            Puzzle.parse_input(puzzle_input)

    # Example input provided in prompt
    def test_solve(self):
        puzzle_input = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3\n"
        expected = 11
        assert Puzzle.solve(puzzle_input) == expected
