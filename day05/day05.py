#!/usr/bin/env python3
import fileinput


def part1(line):

    l = [ord(x) for x in line]
    destroy = [True]
    while any(destroy):
        destroy = [False] * len(l)
        skip = False
        for i, (t, n) in enumerate(zip(l[:-1], l[1:])):
            if skip:
                skip = False
                continue
            if abs(t - n) == 32:
                destroy[i] = True
                destroy[i+1] = True
                skip = True

        l = [ll for ll, dd in zip(l, destroy) if not dd]

    return len(l)


def part2(line):
    
    ls = []
    
    for c in range(65, 65+26):
        l = line.replace(chr(c), "")
        l = l.replace(chr(c+32), "")
        ls.append(part1(l))

    return min(ls)

if __name__ == '__main__':
    line = [x.strip() for x in fileinput.input()][0]
    print("Part 1:", part1(line))
    print("Part 2:", part2(line))
