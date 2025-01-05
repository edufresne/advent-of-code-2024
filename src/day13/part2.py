from fractions import Fraction
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

    def __str__(self):
        return (
            f"Button A: X+{self.a_x}, Y+{self.a_y}\n"
            + f"Button B: {self.b_x}, Y+{self.b_y}\n"
            + f"Prize: X={self.prize_x}, Y={self.prize_y}\n"
        )

    def __repr__(self):
        return self.__str__()


"""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

94*A + 22*B=8400
34*A + 67*B=5400

A = (8400 -22B)/94
34(8400 - 22B)/94 + 67B = 5400
34*8400/94 - 34*22/94B + 67B = 5400
B(67 - 34*22/94)= 5400 - (34*8400/94)
B = (5400 - 34*8400/94) / (67 - 34*22/94)

p_x = A*a_x + B*b_x
p_y = A*a_y + B*b_y

A = (p_x - B*b_x) / a_x

p_y = a_y * ((p_x - B*b_x) / a_x) + B*b_y
p_y = a_y * (p_x/a_x - B*b_x/a_x) + B*b_y
p_y = a_y * p_x / a_x - a_y * b_x * B /a_x + B*b_y
(p_y - a_y * p_x / a_x) / ((b_y - a_y) / a_x * b_x) = B

"""


_BUTTON_RE = re.compile(r"Button.+: X\+(\d+), Y\+(\d+)")
_PRIZE_RE = re.compile(r"Prize: X=(\d+), Y=(\d+)")
_CONVERSION_INCREMENT = 10000000000000


def solve(prize: Prize) -> int:
    print(prize)
    b_presses = (prize.prize_y - (prize.a_y * prize.prize_x / prize.a_x)) / (
        prize.b_y - (prize.a_y * prize.b_x / prize.a_x)
    )
    if b_presses.denominator != 1 or b_presses.numerator <= 0:
        return 0
    a_presses = (prize.prize_y - b_presses * prize.b_y) / prize.a_y
    if a_presses.denominator != 1 or a_presses.numerator <= 0:
        return 0

    print((a_presses, b_presses))

    return 3 * a_presses + b_presses


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
                a_x=Fraction(a_button.group(1)),
                a_y=Fraction(a_button.group(2)),
                b_x=Fraction(b_button.group(1)),
                b_y=Fraction(b_button.group(2)),
                prize_x=Fraction(int(prize.group(1))) + Fraction(_CONVERSION_INCREMENT),
                prize_y=Fraction(int(prize.group(2))) + Fraction(_CONVERSION_INCREMENT),
            )
        )

    for prize in prizes:
        result += solve(prize)
    print(int(result))
