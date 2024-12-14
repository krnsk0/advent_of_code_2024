# https://adventofcode.com/2024/day/9

from _helpers import get_input


def parse(input):
    """
    will generate list with these tuples
    ("free", length)
    ("written", length, id)
    """
    out = []
    for i, n in enumerate(input):
        if i % 2 == 0:
            out.append(("w", int(n), i // 2))
        else:
            out.append(("f", int(n), None))
    return out


def debug(parsed):
    out = ""
    for p in parsed:
        if p[0] == "w":
            out += str(p[2]) * p[1]
        else:
            out += "." * p[1]
    print(out)


def defrag(parsed):
    p = 0
    while p < len(parsed):
        cur = parsed[p]
        if cur[0] == "f":
            # print("\nworking on", cur)

            # find a file from the end
            if parsed[-1][1] == "f":
                # print("found empty space at end; removing")
                parsed.pop()
            last = parsed.pop()
            # print("popped data from end", last)

            if last[0] == "f":
                p + 1
                continue

            # if free space is equal to popped file
            if cur[1] == last[1]:
                # print("equal")
                if p < len(parsed):
                    parsed[p] = ("w", cur[1], last[2])
                else:
                    parsed.append(("w", cur[1], last[2]))

            # if free space is smaller than popped file..
            elif cur[1] < last[1]:
                # print("free is smaller")
                fileRemaining = last[1] - cur[1]
                parsed[p] = ("w", cur[1], last[2])
                parsed.append(("w", fileRemaining, last[2]))

            # if free space is larger than popped file...
            else:
                # print("free is larger")
                spaceRemaining = cur[1] - last[1]
                parsed[p] = ("w", last[1], last[2])
                parsed.insert(p + 1, ("f", spaceRemaining, None))

            # print(parsed)
            # debug(parsed)
        p += 1


def getBlocks(parsed):
    b = 0
    out = []
    for _, size, id in parsed:
        for x in range(size):
            out.append(int(id))
    return out


def getChecksum(parsed):
    checksum = 0
    blocks = getBlocks(parsed)
    for pos, id in enumerate(blocks):
        checksum += pos * id
    return checksum


def solve(input):
    parsed = parse(input)
    # debug(parsed)
    defrag(parsed)
    return getChecksum(parsed)


print("\npart 1 solution:", solve(get_input(use_real=True)))
