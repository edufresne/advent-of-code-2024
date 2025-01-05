import utils


def blink_stone(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    s = str(stone)
    if len(s) % 2 == 0:
        return [int(s[: len(s) // 2]), int(s[len(s) // 2 :])]

    return [stone * 2024]


def blink_stones(stones: list[int]):
    new_stones = []
    for stone in stones:
        new_stones.extend(blink_stone(stone))

    return new_stones


def print_result(stones: list[int]):
    print(" ".join([str(item) for item in stones]))


def run():
    text = utils.get_text(11)
    stones = [int(item) for item in text.split()]
    print_result(stones)
    for i in range(25):
        stones = blink_stones(stones)
        print_result(stones)

    print(len(stones))
