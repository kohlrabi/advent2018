#!/usr/bin/env python3
import fileinput

def freqs(lines):
    freq = 0
    for line in lines:
        op = line[0]
        num = int(line[1:])
        if op == "+":
            freq += num
        else:
            freq -= num
        yield freq

def part1(lines):
    f = 0
    for fr in freqs(lines):
        f = fr
    return f

def part2(lines):
    import itertools

    s = set()
    l = itertools.cycle(lines)
    for fr in freqs(l):
        if fr not in s:
            s.add(fr)
        else:
            return fr

if __name__ == '__main__':
    lines = [x.strip() for x in fileinput.input()]
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
