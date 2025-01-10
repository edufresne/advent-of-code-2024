import re
from typing import Final

import utils

_WIDTH: Final[int] = 101
_HEIGHT: Final[int] = 103

_REGEX = re.compile(r"p=(\d+),(\d+) v=(\-?\d+),(\-?\d+)")


def _visiaulize(positions: list[tuple[int, int]]) -> str:
    matrix = [["." for __ in range(_WIDTH)] for _ in range(_HEIGHT)]
    for x, y in positions:
        matrix[y][x] = "X"

    result = ""
    for item in matrix:
        result += "".join(item) + "\n"
    return result


def run():
    lines = utils.get_input(14)

    positions = {}
    velocities = {}
    for i, line in enumerate(lines):
        matches = _REGEX.match(line)
        positions[i] = (int(matches.group(1)), int(matches.group(2)))
        velocities[i] = (int(matches.group(3)), int(matches.group(4)))

    result = ""
    for seconds in range(1, 101 * 2000):
        potential = seconds >= 72 and (seconds - 72) % 101 == 0
        if potential:
            result += f"Seconds: {seconds}\n"
        for i in range(len(positions)):
            x, y = positions[i]
            dx, dy = velocities[i]
            positions[i] = ((x + dx) % _WIDTH, (y + dy) % _HEIGHT)
        if potential:
            result += _visiaulize(positions.values())

    with open("output.txt", "w+") as f:
        f.write(result)
