from collections import deque
import utils


def run():
    text = utils.get_text(9)
    id_ = 0
    arr = []
    free_space_blocks = deque()
    file_blocks = []
    pos = 0
    for i, text in enumerate(text):
        val = int(text)
        if i % 2 == 0:
            arr.extend([id_] * val)
            file_blocks.append((pos, val, id_))
            id_ += 1
            pos += val
        elif val:
            arr.extend(["."] * val)
            free_space_blocks.append((pos, val))
            pos += val
    print("".join([str(item) for item in arr]))

    while file_blocks:
        file_pos, file_size, file_id = file_blocks.pop()
        free_space_blocks = [
            block for block in free_space_blocks if block[0] < file_pos
        ]
        for i, (free_space_pos, free_space_size) in enumerate(free_space_blocks):
            if file_size <= free_space_size:
                for offset in range(file_size):
                    arr[free_space_pos + offset] = file_id
                    arr[file_pos + offset] = "."
                if file_size == free_space_size:
                    del free_space_blocks[i]
                else:
                    free_space_blocks[i] = (
                        free_space_pos + file_size,
                        free_space_size - file_size,
                    )
                break

    arr = [item for item in arr]
    print("".join([str(item) for item in arr]))
    checksum = 0
    for i, item in enumerate(arr):
        if item != ".":
            checksum += i * item
    print(checksum)
