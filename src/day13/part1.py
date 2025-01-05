"""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

8400
8272 - 94A 0B
8272 - 94A 1B
94
"""

import re
import utils
from dataclasses import dataclass


@dataclass
class Prize:
    a_x: int
    a_y: int
    b_x: int
    b_y: int
    prize_x: int
    prize_y: int


_BUTTON_RE = re.compile(r"Button.+: X\+(\d+), Y\+(\d+)")
_PRIZE_RE = re.compile(r"Prize: X=(\d+), Y=(\d+)")


def solve(prize: Prize) -> int:
    min_combination = None
    min_price = max(prize.prize_x, prize.prize_y)
    for a_presses in range(
        min(prize.prize_x // prize.a_x, prize.prize_y // prize.a_y) + 1
    ):
        for b_presses in range(
            min(prize.prize_x // prize.b_x, prize.prize_y // prize.b_y) + 1
        ):
            if (
                (a_presses * prize.a_x) + (b_presses * prize.b_x) == prize.prize_x
                and (a_presses * prize.a_y) + (b_presses * prize.b_y) == prize.prize_y
                and (3 * a_presses + b_presses) < min_price
            ):
                min_combination = (a_presses, b_presses)
                min_price = 3 * a_presses + b_presses
    print(min_combination)
    return 0 if min_combination is None else min_price


def run():
    lines = utils.get_input(13)
    prizes = []
    result = 0
    for i in range(0, len(lines), 4):
        a_button = _BUTTON_RE.match(lines[i])
        b_button = _BUTTON_RE.match(lines[i + 1])
        prize = _PRIZE_RE.match(lines[i + 2])
        prizes.append(
            Prize(
                a_x=int(a_button.group(1)),
                a_y=int(a_button.group(2)),
                b_x=int(b_button.group(1)),
                b_y=int(b_button.group(2)),
                prize_x=int(prize.group(1)),
                prize_y=int(prize.group(2)),
            )
        )

    for prize in prizes:
        result += solve(prize)
    print(result)
