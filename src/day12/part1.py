from collections import defaultdict, deque
import utils


def get_perimeter(lines: list[str, str], region: set[tuple[int, int]]) -> int:
    result = 0
    for coord in region:
        value = lines[coord[0]][coord[1]]

        # See if on boarder of map. If not see if up/down is the same, if so doesn't need fence.
        if coord[0] == 0:
            result += 1
        elif lines[coord[0] - 1][coord[1]] != value:
            result += 1
        if coord[0] == len(lines) - 1:
            result += 1
        elif lines[coord[0] + 1][coord[1]] != value:
            result += 1

        # Same but for x axis
        if coord[1] == 0:
            result += 1
        elif lines[coord[0]][coord[1] - 1] != value:
            result += 1
        if coord[1] == len(lines) - 1:
            result += 1
        elif lines[coord[0]][coord[1] + 1] != value:
            result += 1

    return result


def get_sides(lines: list[str, str], region: set[tuple[int, int]]) -> int:
    x_sides = 0
    for line_offset in range(len(lines)):
        for string_offset in range(len(lines[0])):
            if (line_offset, string_offset) in region:
                if line_offset == 0 or line_offset == len(lines) - 1:
                    x_sides += 1
                elif string_offset == 0 or string_offset == len(lines[0]) - 1:
                    x_sides += 1


def run():
    lines = utils.get_input(12)

    visited = set()
    region_ids = defaultdict(int)
    regions: dict[tuple[str, int], set[tuple[int, int]]] = defaultdict(set)
    print(f"Lines: {len(lines)}")
    print(f"Length: {len(lines[0])}")
    for line_offset, line in enumerate(lines):
        for string_offset, value in enumerate(line):
            print(f"({line_offset}, {string_offset})")
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
        print(f"Area: {len(values)}")
        print(
            f"Perimeter: {get_perimeter(lines, sorted(values, key=lambda x: x[0] + x[1]))}"
        )
        result += len(values) * get_perimeter(lines, values)
    print(result)
