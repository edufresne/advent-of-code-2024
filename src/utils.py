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
