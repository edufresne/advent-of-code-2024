import utils


def run():
    text = utils.get_text(9)
    id_ = 0
    arr = []
    for i, text in enumerate(text):
        val = int(text)
        if i % 2 == 0:
            arr.extend([id_] * val)
            id_ += 1
        elif val:
            arr.extend(["."] * val)

    l = 0
    r = len(arr) - 1
    while l < r:
        val = arr[r]
        pos = arr[l]
        if val == ".":
            r -= 1
        elif pos != ".":
            l += 1
        else:
            arr[l] = val
            arr[r] = "."
            l += 1
            r -= 1
    arr = [item for item in arr if item != "."]
    print("".join([str(item) for item in arr]))
    checksum = 0
    for i, item in enumerate(arr):
        checksum += i * item
    print(checksum)
