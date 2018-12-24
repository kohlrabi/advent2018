#!/usr/bin/env python3
import fileinput
import re

r = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

def parse(line):
    m = r.match(line)
    return [int(x) for x in m.groups()]

def part1(lines):
    fabric = [[0 for i in range(2000)] for j in range(2000)]

    for line in lines:
        n, l, t, w, h = parse(line)
        for i in range(l, l+w):
            for j in range(t, t+h):
                fabric[i][j] += 1

    s = 0
    for row in fabric:
        for item in row:
            if item > 1:
                s += 1
    return s


def part2(lines):
    fabric = [[[] for i in range(2000)] for j in range(2000)]

    max_n = 0
    for line in lines:
        n, l, t, w, h = parse(line)
        for i in range(l, l+w):
            for j in range(t, t+h):
                fabric[i][j].append(n)
        max_n = n

    for i in range(1, max_n+1):
        found = False
        for row in fabric:
            for item in row:
                if i in item and len(item) > 1:
                    found = True
                    break
            if found:
                break
        else:
            return i

if __name__ == '__main__':
    lines = [x.strip() for x in fileinput.input()]
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
