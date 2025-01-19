import utils


def next_square(
    move: str, current_pos: tuple[int, int], skip: int = 0
) -> tuple[int, int]:
    if move == "<":
        return (current_pos[0], current_pos[1] - 1 - skip)
    elif move == ">":
        return (current_pos[0], current_pos[1] + 1 + skip)
    elif move == "^":
        return (current_pos[0] - 1 - skip, current_pos[1])
    elif move == "v":
        return (current_pos[0] + 1 + skip, current_pos[1])
    else:
        raise ValueError(f"Invalid move: {move}")


def shift_all(m: list[list[str]], move: str, boxes: list[tuple[int, int]]) -> None:
    if move == ">":
        shift = 1
    elif move == "<":
        shift = -1
    else:
        raise NotImplementedError()
    while boxes:
        box = boxes.pop()
        next_line_offset, next_string_offset = next_square(move, box)
        m[next_line_offset][next_string_offset] = "["
        m[next_line_offset][next_string_offset + shift] = "]"
        m[box[0]][box[1]] = "."


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
            chars = []
            for c in line:
                match c:
                    case ".":
                        chars.extend([".", "."])
                    case "@":
                        chars.extend(["@", "."])
                    case "#":
                        chars.extend(["#", "#"])
                    case "O":
                        chars.extend(["[", "]"])
            m.append(chars)
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
        boxes_to_shift = []  # Left edge tuple coords
        match m[start_line_offset][start_string_offset]:
            case ".":
                current_position = start_line_offset, start_string_offset
            case "[" | "]":
                if move in "<>":
                    end_line_offset, end_string_offset = next_square(
                        move, (start_line_offset, start_string_offset)
                    )
                    while (
                        m[end_line_offset][end_string_offset]
                        == m[start_line_offset][
                            start_string_offset
                        ]  # While pointer is at the left/right of box
                    ):
                        boxes_to_shift.append((end_line_offset, end_string_offset))
                        end_line_offset, end_string_offset = next_square(
                            move, (end_line_offset, end_string_offset), skip=1
                        )
                    if m[end_line_offset][end_string_offset] == ".":
                        current_position = start_line_offset, start_string_offset
                        shift_all(m, move, boxes_to_shift)
                else:
                    if m[start_line_offset][start_string_offset] == "]":
                        right_ptr = (start_line_offset, start_string_offset)
                        left_ptr = (start_line_offset, start_string_offset - 1)
                    else:
                        left_ptr = (start_line_offset, start_string_offset)
                        right_ptr = (start_line_offset, start_string_offset + 1)
                    boxes_to_shift.append((start_line_offset, start_string_offset))

                    while left_ptr != right_ptr:
                        next_left = next_square(left_ptr)
                        next_right = next_square(right_ptr)
                        next_left_val = m[next_left[0]][next_left[1]]
                        next_right_val = m[next_right[0]][next_right[1]]
                        if next_left_val == "]":
                            next_left -= 1
                            boxes_to_shift.append(())

        visualize(m, current_position)

    result = 0
    for line_offset in range(len(m)):
        for string_offset in range(len(m[0])):
            if m[line_offset][string_offset] == "O":
                result += 100 * line_offset + string_offset
    print(result)
