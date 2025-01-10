import re
from typing import Final

import utils

_WIDTH: Final[int] = 101
_HEIGHT: Final[int] = 103
_NUM_SECONDS: Final[int] = 100

_REGEX = re.compile(r"p=(\d+),(\d+) v=(\-?\d+),(\-?\d+)")


def _visiaulize(positions: list[tuple[int, int]]):
    matrix = [["." for _ in range(_WIDTH)] for _ in range(_HEIGHT)]
    for x, y in positions:
        matrix[y][x] = "X"

    for item in matrix:
        print("".join(item))


def run():
    lines = utils.get_input(14)

    positions = {}
    velocities = {}
    for i, line in enumerate(lines):
        matches = _REGEX.match(line)
        positions[i] = (int(matches.group(1)), int(matches.group(2)))
        velocities[i] = (int(matches.group(3)), int(matches.group(4)))

    for _ in range(_NUM_SECONDS):
        _visiaulize(positions.values())
        for i in range(len(positions)):
            x, y = positions[i]
            dx, dy = velocities[i]
            positions[i] = ((x + dx) % _WIDTH, (y + dy) % _HEIGHT)

    top_left, top_right, bottom_left, bottom_right = 0, 0, 0, 0
    for position in sorted(positions.values(), key=lambda x: x[1] * 10 + x[0]):
        print(position)
        x, y = position
        if x < _WIDTH // 2 and y < _HEIGHT // 2:
            top_left += 1
        elif x < _WIDTH // 2 and y > _HEIGHT // 2:
            bottom_left += 1
        elif x > _WIDTH // 2 and y < _HEIGHT // 2:
            top_right += 1
        elif x > _WIDTH // 2 and y > _HEIGHT // 2:
            bottom_right += 1
    print(f"Top left: {top_left}")
    print(f"Top right: {top_right}")
    print(f"Bottom left: {bottom_left}")
    print(f"Bottom right: {bottom_right}")

    print(top_left * top_right * bottom_left * bottom_right)
