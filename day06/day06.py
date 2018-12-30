#!/usr/bin/env python3
import fileinput
import numpy as np
import re

def manhattan(x, y, tx, ty):
    return np.abs(tx-x, dtype=int) + np.abs(ty-y, dtype=int)

def coords_grid(lines):
    r = re.compile(r"(\d+),\s*(\d+)")

    coords = np.array([tuple(map(int, r.match(l).groups())) for l in lines])

    xc = coords[:,0]
    yc = coords[:,1]
    max_x = xc.max() + 1
    max_y = yc.max() + 1
    
    grid = np.zeros((max_x, max_y), dtype=int)

    return coords, grid


def part1(lines):

    coords, grid = coords_grid(lines)

    lc = coords.shape[0]
    max_x, max_y = grid.shape

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
    
    coords, grid = coords_grid(lines)
    
    max_x, max_y = grid.shape
    
    for i in range(max_x):
        for j in range(max_y):
            m = [manhattan(i, j, *c) for c in coords]
            if np.sum(m) < 10000:
                grid[i,j] = 1

    return np.sum(grid)

if __name__ == '__main__':
    lines = [x.strip() for x in fileinput.input()]
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
