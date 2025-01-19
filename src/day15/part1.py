import utils


def next_square(move: str, current_pos: tuple[int, int]) -> tuple[int, int]:
    if move == "<":
        return (current_pos[0], current_pos[1] - 1)
    elif move == ">":
        return (current_pos[0], current_pos[1] + 1)
    elif move == "^":
        return (current_pos[0] - 1, current_pos[1])
    elif move == "v":
        return (current_pos[0] + 1, current_pos[1])
    else:
        raise ValueError(f"Invalid move: {move}")


def visualize(m, current_position):
    for line_offset in range(len(m)):
        line = ""
        for string_offset in range(len(m[0])):
            if (line_offset, string_offset) == current_position:
                line += "@"
            else:
                line += m[line_offset][string_offset]
        print(line)


def run():
    lines = utils.get_input(15)
    m = []
    moves = ""
    map_tiles = True
    for line in lines:
        if not line.strip():
            map_tiles = False
        elif map_tiles:
            m.append([c for c in line])
        else:
            moves += line

    current_position = None
    for line_offset in range(len(m)):
        for string_offset in range(len(m[0])):
            if m[line_offset][string_offset] == "@":
                current_position = (line_offset, string_offset)
                m[line_offset][string_offset] = "."
                break

    visualize(m, current_position)
    for move in moves:
        start_line_offset, start_string_offset = next_square(move, current_position)
        match m[start_line_offset][start_string_offset]:
            case ".":
                current_position = start_line_offset, start_string_offset
            case "O":
                end_line_offset, end_string_offset = next_square(
                    move, (start_line_offset, start_string_offset)
                )
                while m[end_line_offset][end_string_offset] == "O":
                    end_line_offset, end_string_offset = next_square(
                        move, (end_line_offset, end_string_offset)
                    )
                if m[end_line_offset][end_string_offset] == ".":
                    current_position = start_line_offset, start_string_offset
                    m[start_line_offset][start_string_offset] = "."
                    m[end_line_offset][end_string_offset] = "O"
        visualize(m, current_position)

    result = 0
    for line_offset in range(len(m)):
        for string_offset in range(len(m[0])):
            if m[line_offset][string_offset] == "O":
                result += 100 * line_offset + string_offset
    print(result)
