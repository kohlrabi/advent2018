#!/usr/bin/env python3
import fileinput
import numpy as np
import re

def manhattan(x, y, tx, ty):
    return np.abs(tx-x, dtype=int) + np.abs(ty-y, dtype=int)

def part1(lines):

    r = re.compile(r"(\d+),\s*(\d+)")

    coords = np.array([tuple(map(int, r.match(l).groups())) for l in lines])
    lc = coords.shape[0]

    xc = coords[:,0]
    yc = coords[:,1]
    max_x = xc.max() + 1
    max_y = yc.max() + 1
    grid = np.zeros((max_x, max_y), dtype=int)

    for i in range(max_x):
        for j in range(max_y):
            m = [manhattan(i, j, *c) for c in coords]
            s = np.sort(m)
            if s[0] == s[1]:
                grid[i,j] = lc+1
            else:
                grid[i,j] = np.argmin(m)

    counts = np.bincount(grid.ravel())[:-1]

    for i in range(lc):
        if np.any(grid[0,:]==i) or np.any(grid[-1,:]==i) or np.any(grid[:,0]==i) or np.any(grid[:,-1]==i):
            counts[i]=0
    
    return np.max(counts)


def part2(lines):

    return

if __name__ == '__main__':
    lines = [x.strip() for x in fileinput.input()]
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
