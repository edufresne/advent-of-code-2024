from pathlib import Path


def get_input(day: int) -> list[str]:
    p = Path(__file__).parents[1].joinpath("inputs", f"puzzle_input{day}")
    return p.read_text().splitlines()
