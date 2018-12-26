#!/usr/bin/env python3
import fileinput
import re

r = re.compile(r"\[(.*)] (.*)")

def parse(line):
    m = r.match(line)
    return m.groups()

def prep(lines):
    import datetime

    cron = []
    for line in lines:
        t, a = parse(line)
        t = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M")
        if a.startswith("falls"):
            a = -1
        elif a.startswith("wakes"):
            a = -2
        else:
            a = int(a.split()[1][1:])
        cron.append((t, a))

    cron = sorted(cron, key=lambda x: x[0])
    
    active = None
    guards = {}
    s = 0
    e = 0
    for t, a in cron:
        if a >= 0:
            if s:
                e = t.minute
                for i in range(s, e):
                    guards[active][i] += 1
            active = a
            if a not in guards:
                guards.update({a: [0 for i in range(60)]})
        if a == -1:
            s = t.minute
            e = None
        if a == -2:
            e = t.minute
            for i in range(s, e):
                guards[active][i] += 1
            s = None

    return guards
    
def part1(lines):
    guards = prep(lines)

    m = 0
    mi = -1
    mm = -1
    for k, v in guards.items():
        sv = sum(v)
        if sv > m:
            mi = k
            m = sv
            mm = max(zip(v, range(60)))[-1]

    checksum = mi * mm
    return checksum

def part2(lines):
    guards = prep(lines)

    m = (-1, -1)
    mi = -1
    for k, v in guards.items():
        for i, vv in enumerate(v):
            if vv > m[1]:
                mi = k
                m = (i, vv)

    checksum = mi * m[0]
    return checksum


if __name__ == '__main__':
    lines = [x.strip() for x in fileinput.input()]
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
