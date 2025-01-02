import utils


def get_next_coords(lines: [list[str]], pos: tuple[int, int]):
    return [
        item
        for item in [
            (pos[0], pos[1] + 1),
            (pos[0], pos[1] - 1),
            (pos[0] + 1, pos[1]),
            (pos[0] - 1, pos[1]),
        ]
        if 0 <= item[0] < len(lines) and 0 <= item[1] < len(lines[0])
    ]


def get_score(lines: list[list[str]], trailhead: tuple[int, int]) -> int:
    print(f"Trailhead: {trailhead}")
    q = get_next_coords(lines, trailhead)
    last_height = 0
    peaks = set()
    while q:
        current_items = q
        q = []
        for item in current_items:
            height_val = int(lines[item[0]][item[1]])
            if height_val - last_height == 1:
                print(f"Visited: {item}: {height_val} at current height: {last_height}")
                if height_val == 9:
                    peaks.add(item)
                else:
                    q.extend(get_next_coords(lines, item))

        last_height += 1
    print(f"Trailehead: {trailhead}, score: {len(peaks)}")
    return len(peaks)


def run():
    lines = utils.get_input(10)
    trailheads = set()
    for line_offset in range(len(lines)):
        for string_offset in range(len(lines[0])):
            val = lines[line_offset][string_offset]
            if val == "0":
                trailheads.add((line_offset, string_offset))

    result = 0
    for trailhead in trailheads:
        result += get_score(lines, trailhead)

    print(result)
