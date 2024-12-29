import itertools
import utils


def solve(answer: int, numbers: list[int]) -> bool:
    combinations = list(
        itertools.product(*[["+", "*"] for _ in range(len(numbers) + 1)])
    )
    for combination in combinations:
        total = numbers[0]
        for i, operator in enumerate(combination[1:-1]):
            if operator == "*":
                total *= numbers[i + 1]
            else:
                total += numbers[i + 1]
        if total == answer:
            return True

    return False


def run():
    lines = utils.get_input(7)
    equations = {}
    for line in lines:
        answer, equation = line.split(":")
        equations[int(answer)] = [int(num) for num in equation.split()]

    result = 0
    for answer, numbers in equations.items():
        if solve(answer, numbers):
            result += answer
        print(result)

    print(result)
