from pathlib import Path


def get_input(day: int) -> list[str]:
    return get_text().splitlines()


def get_text(day: int) -> str:
    p = Path(__file__).parents[1].joinpath("inputs", f"puzzle_input{day}")
    return p.read_text()
