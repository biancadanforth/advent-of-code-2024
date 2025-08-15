from day01 import Puzzle


class TestPuzzle(object):
    def test_example_1(self):
        puzzle_input = "abcdef"
        expected = 1
        assert Puzzle.solve(puzzle_input) == expected

    def test_example_2(self):
        puzzle_input = "pqrstuv"
        expected = 1
        assert Puzzle.solve(puzzle_input) == expected
