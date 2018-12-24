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
    for i, l1 in enumerate(lines[:-1]):
        for l2 in lines[i+1:]:
            d = []
            for j, (c1, c2) in enumerate(zip(l1, l2)):
                if c1 != c2:
                    d.append(j)
            if len(d) == 1:
                return l1[:d[0]] + l1[d[0]+1:]

if __name__ == '__main__':
    lines = [x.strip() for x in fileinput.input()]
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
