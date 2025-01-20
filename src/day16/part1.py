from collections import defaultdict, deque
from src.utils import Direction, get_input, get_next_compass_coords


def get_paths(lines, pos, direction: Direction = None):
    coords = get_next_compass_coords(lines, pos)
    return {
        k: v
        for k, v in coords.items()
        if lines[v[0]][v[1]] != "#" and direction is None or k != direction.backwards
    }


def score_to_next_vertex(
    lines, pos, direction: Direction
) -> tuple[tuple[int, int], Direction, int] | None:
    score = 0
    while True:
        coords = get_next_compass_coords(lines, pos, direction)
        score += 1
        if len(coords) == 0:
            return None
        if len(coords) > 1:
            return pos, direction, score
        pos = coords.values()[0]
        if direction not in coords[direction]:
            direction = coords.keys()[0]
            score += 1000


def run():
    m = get_input(16)
    starting_position = None
    ending_position = None
    for line_offset in range(len(m)):
        for string_offset in range(len(m[0])):
            if m[line_offset][string_offset] == "S":
                starting_position = line_offset, string_offset
            elif m[line_offset][string_offset] == "E":
                ending_position = line_offset, string_offset
    assert starting_position and ending_position

    graph = defaultdict(dict)
    graph[starting_position] = {}
    direction = Direction.E
    q = deque()
    q.append(starting_position)
    position = starting_position
    while True:
        coords = get_paths(starting_position, position)
        for 
        scores = {d: score_to_next_vertex(m, coord, d) for d, coord in coords.items()}
