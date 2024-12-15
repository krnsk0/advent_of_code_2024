# https://adventofcode.com/2024/day/9

from _helpers import get_input


def parse(input):
    """
    will generate list of tuple of type
    (id, length)
    id=None means it is free space
    """
    out = []
    for i, n in enumerate(input):
        if i % 2 == 0:
            out.append((i // 2, int(n)))
        else:
            out.append((None, int(n)))
    return out


def debug(parsed):
    out = ""
    for id, size in parsed:
        if id is None:
            out += size * "."
        else:
            out += str(id) * size
    print(out)


def defrag(parsed):
    j = len(parsed) - 1
    while j >= 0:
        id, size = parsed[j]
        if id is not None:
            # print(f"\nlooking for space for file {id} with size {size}")
            i = 0
            while i < j:
                destId, destSize = parsed[i]
                if destId == None:
                    # print(f"checking against {i}, size {destSize}")
                    if destSize == size:
                        # print(f"found spot at {i}; same size")
                        parsed[i] = (id, size)
                        parsed[j] = (None, size)
                        # debug(parsed)
                        break
                    elif size < destSize:
                        # print(f"found spot at {i}; file is smaller than space")
                        diff = destSize - size
                        parsed[j] = (None, size)
                        parsed[i] = (id, size)
                        parsed.insert(i + 1, (None, diff))
                        # debug(parsed)
                        break
                i += 1
        j -= 1


def getChecksum(parsed):
    # id
    blocks = []
    for id, size in parsed:
        for _ in range(size):
            if id is not None:
                blocks.append(id)
            else:
                blocks.append(0)

    checksum = 0
    for i, id in enumerate(blocks):
        checksum += i * id

    return checksum


def solve(input):
    parsed = parse(input)
    print("input:")
    debug(parsed)
    defrag(parsed)
    print("\ndefragged:")
    debug(parsed)
    return getChecksum(parsed)


print("\npart 1 solution:", solve(get_input(use_real=True)))
