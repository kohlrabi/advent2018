#!/usr/bin/env python3
import fileinput

def hist(line):
    import collections
    
    d = collections.defaultdict(lambda: 0)
    for c in line:
        d[c] += 1

    return d

def part1(lines):
    twos, threes = 0, 0
    for line in lines:
        h = hist(line)
        v = h.values()
        if 2 in v:
            twos += 1
        if 3 in v:
            threes += 1
    return twos * threes

def part2(lines):
    pass

if __name__ == '__main__':
    lines = [x for x in fileinput.input()]
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
