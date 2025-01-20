from enum import StrEnum
from pathlib import Path


def get_input(day: int) -> list[str]:
    return get_text(day).splitlines()


def get_text(day: int) -> str:
    p = Path(__file__).parents[1].joinpath("inputs", f"puzzle_input{day}")
    return p.read_text()


def get_next_coords(lines: [list[str]], pos: tuple[int, int]):
    return [
        item
        for item in [
            (pos[0], pos[1] + 1),
            (pos[0], pos[1] - 1),
            (pos[0] + 1, pos[1]),
            (pos[0] - 1, pos[1]),
        ]
        if 0 <= item[0] < len(lines) and 0 <= item[1] < len(lines[0])
    ]


class Direction(StrEnum):
    N = "N"
    E = "E"
    S = "S"
    W = "W"

    @property
    def backwards(self):
        match self:
            case self.N:
                return self.S
            case self.S:
                return self.N
            case self.E:
                return self.W
            case self.W:
                return self.E
        raise NotImplementedError()


def get_next_compass_coords(
    lines: [list[str]], pos: tuple[int, int]
) -> dict[Direction, tuple[int, int]]:
    coords = {
        Direction.E: (pos[0], pos[1] + 1),
        Direction.W: (pos[0], pos[1] - 1),
        Direction.N: (pos[0] + 1, pos[1]),
        Direction.S: (pos[0] - 1, pos[1]),
    }

    return {
        k: v
        for k, v in coords.items()
        if 0 <= v[0] < len(lines) and 0 <= v[1] < len(lines[0])
    }
