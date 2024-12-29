from collections import defaultdict
import itertools
import re
import utils


_ANTENNA_REGEX = re.compile(r"^[a-zA-Z0-9]+$")


def run():
    lines = utils.get_input(8)
    antenna_map = defaultdict(set)
    for line_offset in range(len(lines)):
        for string_offset in range(len(lines[0])):
            frequency = lines[line_offset][string_offset]
            if _ANTENNA_REGEX.match(frequency):
                antenna_map[frequency].add((line_offset, string_offset))

    antinodes = set()
    for _, antenna_locations in antenna_map.items():
        if antenna_locations:
            combinations = itertools.combinations(antenna_locations, 2)
            for combination in combinations:
                antinode_1 = (
                    2 * combination[0][0] - combination[1][0],
                    2 * combination[0][1] - combination[1][1],
                )
                antinode_2 = (
                    2 * combination[1][0] - combination[0][0],
                    2 * combination[1][1] - combination[0][1],
                )
                if 0 <= antinode_1[0] < len(lines) and 0 <= antinode_1[1] < len(
                    lines[0]
                ):
                    antinodes.add(antinode_1)
                if 0 <= antinode_2[0] < len(lines) and 0 <= antinode_2[1] < len(
                    lines[0]
                ):
                    antinodes.add(antinode_2)
    print(antinodes)
    print(len(antinodes))
