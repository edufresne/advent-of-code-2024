from collections import defaultdict
import itertools
import re
import utils


_ANTENNA_REGEX = re.compile(r"^[a-zA-Z0-9]+$")


def run():
    lines = utils.get_input(8)
    antenna_map = defaultdict(set)
    solution = set()
    for line_offset in range(len(lines)):
        for string_offset in range(len(lines[0])):
            frequency = lines[line_offset][string_offset]
            if _ANTENNA_REGEX.match(frequency):
                antenna_map[frequency].add((line_offset, string_offset))
            if frequency == "#":
                solution.add((line_offset, string_offset))

    antinodes = set()
    for frequency, antenna_locations in antenna_map.items():
        if antenna_locations:
            print(f"Frequency: {frequency}")
            combinations = itertools.combinations(antenna_locations, 2)
            for combination in combinations:
                antinodes.add(combination[0])
                antinodes.add(combination[1])
                print(f"Antinodes for: {combination}")
                diffs = (
                    combination[1][0] - combination[0][0],
                    combination[1][1] - combination[0][1],
                )
                antinode_1 = (
                    combination[0][0] - diffs[0],
                    combination[0][1] - diffs[1],
                )
                while 0 <= antinode_1[0] < len(lines) and 0 <= antinode_1[1] < len(
                    lines[0]
                ):
                    print(antinode_1)
                    antinodes.add(antinode_1)
                    antinode_1 = (antinode_1[0] - diffs[0], antinode_1[1] - diffs[1])

                antinode_2 = (
                    combination[1][0] + diffs[0],
                    combination[1][1] + diffs[1],
                )
                while 0 <= antinode_2[0] < len(lines) and 0 <= antinode_2[1] < len(
                    lines[0]
                ):
                    print(antinode_2)
                    antinodes.add(antinode_2)
                    antinode_2 = (
                        antinode_2[0] + diffs[0],
                        antinode_2[1] + diffs[1],
                    )
    print(sorted(antinodes))
    print(len(antinodes))
    print(sorted([item for item in solution if item not in antinodes]))
