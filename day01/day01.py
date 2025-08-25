import os
import re


class Puzzle:
    @classmethod
    def parse_input(cls, puzzle_input):
        """
        Takes a multiline string puzzle input and returns a 2-tuple of lists of
        location IDs.

        :arg puzzle_input: Multiline string, where each line contains two sets
        of positive, whole numbers separated by one or more non-digit characters
        (e.g. spaces).
        Invalid lines in the string will throw a ValueError. If more than two sets of
        digits are in a line, only the first two sets are used.

        :returns: Tuple[list[int], list[int]]
        Each list consists of a set of location IDs. The first list represents those
        from the first column, and the second list represents
        those from the second column in the puzzle input.
        The lists in the tuple are of equal length.
        """
        first_list = []
        second_list = []
        for line in puzzle_input.splitlines():
            line = line.strip()
            # capture each pair of digits per line, ignoring any other chars
            match = re.match(r".*?(\d+).*?(\d+).*", line)
            if match:
                first_match, second_match = match.groups()
                first_list.append(int(first_match))
                second_list.append(int(second_match))
            else:
                raise ValueError(f"One or both values missing in line: {line}.")
        return (first_list, second_list)

    @classmethod
    def solve_part_1(cls, puzzle_input):
        (first_list, second_list) = cls.parse_input(puzzle_input)
        first_list.sort()
        second_list.sort()
        total_distance = 0
        for first_id, second_id in zip(first_list, second_list):
            diff = abs(first_id - second_id)
            total_distance += diff
        return total_distance

    @classmethod
    def solve_part_2(cls, puzzle_input):
        (first_list, second_list) = cls.parse_input(puzzle_input)
        total_similarity_score = 0
        # make an int:int map for the second list of location_id
        # to frequency.
        second_list_histogram = dict()
        for location_id in second_list:
            if location_id in second_list_histogram:
                second_list_histogram[location_id] += 1
            else:
                second_list_histogram[location_id] = 1
        for location_id in first_list:
            if location_id in second_list_histogram:
                total_similarity_score += (
                    location_id * second_list_histogram[location_id]
                )
        return total_similarity_score


def main():
    path = os.path.join(os.path.dirname(__file__), "input")
    with open(path) as f:
        puzzle_input = f.read()
    print(Puzzle.solve_part_1(puzzle_input))
    print(Puzzle.solve_part_2(puzzle_input))


if __name__ == "__main__":
    main()
