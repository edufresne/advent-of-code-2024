from collections import defaultdict, deque
import utils


def get_sides(lines: list[str, str], value: str, region: set[tuple[int, int]]) -> int:
    result = 0
    for line_offset in range(len(lines)):
        exists_above, exists_below = False, False
        for string_offset in range(len(lines[0])):
            above, below = (
                (line_offset - 1, string_offset),
                (line_offset + 1, string_offset),
            )
            if (line_offset, string_offset) not in region:
                if line_offset == 0:
                    exists_above = False
                if line_offset == len(lines) - 1:
                    exists_below = False
                continue

            if line_offset == 0:
                if not exists_above:
                    result += 1
                    exists_above = True
            elif lines[above[0]][above[1]] != value and not exists_above:
                exists_above = True
                result += 1
            elif lines[above[0]][above[1]] == value:
                exists_above = False

            if line_offset == len(lines) - 1:
                if not exists_below:
                    result += 1
                    exists_below = True
            elif lines[below[0]][below[1]] != value and not exists_below:
                exists_below = True
                result += 1
            elif lines[below[0]][below[1]] == value:
                exists_below = False
    print("Left to right")
    for string_offset in range(len(lines[0])):
        exists_left, exists_right = False, False
        for line_offset in range(len(lines)):
            left, right = (
                (line_offset, string_offset - 1),
                (line_offset, string_offset + 1),
            )
            if (line_offset, string_offset) not in region:
                if string_offset == 0:
                    exists_left = False
                if string_offset == len(lines[0]) - 1:
                    exists_right = False
                continue

            if string_offset == 0:
                if not exists_left:
                    print(f"{(line_offset, string_offset)}: +1 Left border")
                    result += 1
                    exists_left = True
            elif lines[left[0]][left[1]] != value and not exists_left:
                print(f"{(line_offset, string_offset)}: +1 Left of square")
                exists_left = True
                result += 1
            elif lines[left[0]][left[1]] == value:
                exists_left = False

            if string_offset == len(lines[0]) - 1:
                if not exists_right:
                    print(f"{(line_offset, string_offset)}: +1 Right border")
                    result += 1
                    exists_right = True
            elif lines[right[0]][right[1]] != value and not exists_right:
                print(f"{(line_offset, string_offset)}: +1 Right of square")
                exists_right = True
                result += 1
            elif lines[right[0]][right[1]] == value:
                exists_right = False
    return result


def run():
    lines = utils.get_input(12)

    visited = set()
    region_ids = defaultdict(int)
    regions: dict[tuple[str, int], set[tuple[int, int]]] = defaultdict(set)
    print(f"Lines: {len(lines)}")
    print(f"Length: {len(lines[0])}")
    for line_offset, line in enumerate(lines):
        for string_offset, value in enumerate(line):
            if (line_offset, string_offset) in visited:
                continue

            if (value, region_ids[value]) not in regions:
                # New Region found
                coords = utils.get_next_coords(lines, (line_offset, string_offset))
                q = deque(
                    [coord for coord in coords if lines[coord[0]][coord[1]] == value]
                )
                visited.add((line_offset, string_offset))
                regions[(value, region_ids[value])].add((line_offset, string_offset))
                while q:
                    if len(q) % 1000 == 0:
                        print(len(q))
                    current_position = q.popleft()
                    regions[(value, region_ids[value])].add(current_position)
                    visited.add(current_position)
                    q.extend(
                        [
                            coord
                            for coord in utils.get_next_coords(lines, current_position)
                            if coord not in visited
                            and lines[coord[0]][coord[1]] == value
                            and coord not in q
                        ]
                    )
                region_ids[value] += 1

    result = 0
    for region, values in regions.items():
        print(f"{region[0]}{region[1]}: {sorted(values, key=lambda x: x[0] + x[1])}")
        sides = get_sides(lines, region[0], values)
        print(f"Area: {len(values)}")
        print(f"Sides: {sides}")
        result += sides * len(values)

    print(result)
