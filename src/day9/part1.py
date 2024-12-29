from collections import deque
import utils


def run():
    text = utils.get_text(9)
    id_ = 0
    pos = 0
    arr = []
    free_space = deque()
    for i, text in enumerate(text):
        val = int(text)
        if i % 2 == 0:
            arr.extend([id_] * val)
            id_ += 1
            pos += val
        elif val:
            arr.extend(["."] * val)
            free_space.append((pos, val))
            pos += val

    i = len(arr) - 1
    while free_space:
        pos, space = free_space.popleft()
        for offset in range(space):
            val_to_move = arr[i]
            while val_to_move == ".":
                i -= 1
                val_to_move = arr[i]
            arr[pos + offset] = arr[i]
            arr[i] = "."
            i -= 1
    print(arr)
    arr = [item for item in arr if item != "."]
    checksum = 0
    for i, val in enumerate(arr):
        checksum += (i) * val
    print(checksum)
