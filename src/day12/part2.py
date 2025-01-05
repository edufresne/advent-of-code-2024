from collections import defaultdict, deque
import utils


def get_sides(lines: list[str, str], value: str, region: set[tuple[int, int]]) -> int:
    result = 0
    sides = set()
    for line_offset in range(len(lines)):
        for string_offset in range(len(lines[0])):
            if (line_offset, string_offset) not in region:
                if line_offset == 0:
                    sides.discard(0)
                elif line_offset == len(lines) - 1:
                    sides.discard(len(lines) - 1)
                continue

            above, below = (
                (line_offset - 1, string_offset),
                (line_offset + 1, string_offset),
            )
            if line_offset != 0:
                if lines[above[0]][above[1]] != value and line_offset not in sides:
                    sides.add(line_offset)
                    result += 1
                elif lines[above[0]][above[1]] == value:
                    sides.discard(line_offset)
            elif 0 not in sides:
                sides.add(0)
                result += 1

            if line_offset != len(lines) - 1:
                if lines[below[0]][below[1]] != value and line_offset + 1 not in sides:
                    sides.add(line_offset + 1)
                    result += 1
                elif lines[below[0]][below[1]] == value:
                    sides.discard(line_offset + 1)
            elif len(lines) not in sides:
                sides.add(len(lines))
                result += 1

    sides = set()
    for string_offset in range(len(lines[0])):
        for line_offset in range(len(lines)):
            if (line_offset, string_offset) not in region:
                if string_offset == 0:
                    sides.discard(0)
                elif string_offset == len(lines[0]) - 1:
                    sides.discard(len(lines[0]) - 1)
                continue

            left, right = (
                (line_offset, string_offset - 1),
                (line_offset, string_offset + 1),
            )
            if string_offset != 0:
                if lines[left[0]][left[1]] != value and string_offset not in sides:
                    sides.add(string_offset)
                    result += 1
                elif lines[above[0]][above[1]] == value:
                    sides.discard(string_offset)
            elif 0 not in sides:
                sides.add(0)
                result += 1

            if string_offset != len(lines[0]) - 1:
                if (
                    lines[right[0]][right[1]] != value
                    and string_offset + 1 not in sides
                ):
                    sides.add(string_offset + 1)
                    result += 1
                elif lines[right[0]][right[1]] == value:
                    sides.discard(string_offset + 1)
            elif len(lines[0]) not in sides:
                sides.add(len(lines[0]))
                result += 1
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
