import itertools
from typing import Self
import utils
from dataclasses import dataclass


@dataclass
class Stone:
    value: int
    multiplier: int = 1

    def blink_stone(self) -> list[Self]:
        if self.value == 0:
            return [Stone(1, multiplier=self.multiplier)]

        s = str(self.value)
        if len(s) % 2 == 0:
            return [
                Stone(int(s[: len(s) // 2]), self.multiplier),
                Stone(int(s[len(s) // 2 :]), self.multiplier),
            ]

        return [Stone(self.value * 2024, self.multiplier)]


def print_result(stones: list[int]):
    print(" ".join([str(item) for item in stones]))


def run():
    text = utils.get_text(11)
    stones = [int(item) for item in text.split()]
    stones = [Stone(item, stones.count(item)) for item in set(stones)]
    n = 75
    for i in range(n):
        stones = list(
            itertools.chain.from_iterable([stone.blink_stone() for stone in stones])
        )
        unique_values = set(stone.value for stone in stones)
        stones = [
            Stone(
                unique_item,
                sum(stone.multiplier for stone in stones if stone.value == unique_item),
            )
            for unique_item in unique_values
        ]

    print(sum([item.multiplier for item in stones]))
