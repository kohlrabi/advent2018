#!/usr/bin/env python3
import fileinput



def part1(line):

    l = list(line)
    destroy = [True]
    while any(destroy):
        destroy = [False] * len(l)
        skip = False
        for i, (t, n) in enumerate(zip(l[:-1], l[1:])):
            if skip:
                skip = False
                continue
            if t != n and t.lower() == n.lower():
                destroy[i] = True
                destroy[i+1] = True
                skip = True

        l = [ll for ll, dd in zip(l, destroy) if not dd]

    return len(l)


def part2(lines):
   return


if __name__ == '__main__':
    line = [x.strip() for x in fileinput.input()][0]
    print("Part 1:", part1(line))
    print("Part 2:", part2(line))
