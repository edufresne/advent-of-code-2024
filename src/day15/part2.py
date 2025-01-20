import itertools
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


def shift_all_horizontal(
    m: list[list[str]], move: str, boxes: list[tuple[int, int]]
) -> None:
    if move == ">":
        shift = 1
    elif move == "<":
        shift = -1
    else:
        raise NotImplementedError(move)
    while boxes:
        box = boxes.pop()
        next_line_offset, next_string_offset = next_square(move, box)
        m[next_line_offset][next_string_offset] = "[" if move == ">" else "]"
        m[next_line_offset][next_string_offset + shift] = "]" if move == ">" else "["
        if not boxes:
            m[box[0]][box[1]] = "."


def shift_all_vertical(
    m: list[list[str]], move: str, boxes: list[tuple[int, int]]
) -> None:
    if move not in "v^":
        raise NotImplementedError(move)
    while boxes:
        box = boxes.pop()
        next_line_offset, next_string_offset = next_square(move, box)
        m[next_line_offset][next_string_offset] = "["
        m[next_line_offset][next_string_offset + 1] = "]"
        m[box[0]][box[1]] = "."
        m[box[0]][box[1] + 1] = "."


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
        print(f"Move: {move}")
        start_line_offset, start_string_offset = next_square(move, current_position)
        boxes_to_shift = []  # Left edge tuple coords
        match m[start_line_offset][start_string_offset]:
            case ".":
                current_position = start_line_offset, start_string_offset
            case "[" | "]":
                if move in "<>":
                    end_line_offset, end_string_offset = next_square(
                        move, (start_line_offset, start_string_offset), skip=1
                    )
                    boxes_to_shift.append((start_line_offset, start_string_offset))
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
                        shift_all_horizontal(m, move, boxes_to_shift)
                else:
                    boxes_to_shift.append(
                        (start_line_offset, start_string_offset)
                        if m[start_line_offset][start_string_offset] == "["
                        else (start_line_offset, start_string_offset - 1)
                    )
                    last_boxes_layer = {boxes_to_shift[0]}
                    while last_boxes_layer:
                        squares_to_check = list(
                            itertools.chain.from_iterable(
                                [
                                    [
                                        next_square(move, box),
                                        next_square(move, (box[0], box[1] + 1)),
                                    ]
                                    for box in last_boxes_layer
                                ]
                            )
                        )
                        if any(
                            m[square[0]][square[1]] == "#"
                            for square in squares_to_check
                        ):
                            boxes_to_shift = []
                            break
                        elif all(
                            m[square[0]][square[1]] == "."
                            for square in squares_to_check
                        ):
                            current_position = (start_line_offset, start_string_offset)
                            break
                        else:
                            last_boxes_layer = set()
                            for square in squares_to_check:
                                val = m[square[0]][square[1]]
                                if val == "[":
                                    last_boxes_layer.add(square)
                                    boxes_to_shift.append(square)
                                elif val == "]":
                                    last_boxes_layer.add((square[0], square[1] - 1))
                                    boxes_to_shift.append((square[0], square[1] - 1))

                    shift_all_vertical(m, move, boxes_to_shift)

        visualize(m, current_position)

    result = 0
    for line_offset in range(len(m)):
        for string_offset in range(len(m[0])):
            if m[line_offset][string_offset] == "[":
                result += 100 * line_offset + string_offset
    print(result)
