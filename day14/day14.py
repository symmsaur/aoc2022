#!/usr/bin/env python3

import numpy as np
from pprint import pprint
from matplotlib import pyplot


def create_inclusive_range(a, b):
    if a > b:
        return range(b, a + 1)
    return range(a, b + 1)


def parse_sequence(line):
    pairs = [s.split(",") for s in line.split()[::2]]
    return [(int(x) - 300, int(y)) for x, y in pairs]


def draw_segments(grid, line):
    sequence = parse_sequence(line)
    previous = sequence[0]
    for current in sequence[1:]:
        if current[0] == previous[0]:
            x = current[0]
            for y in create_inclusive_range(current[1], previous[1]):
                grid[y, x] = 1
        else:
            y = current[1]
            for x in create_inclusive_range(current[0], previous[0]):
                grid[y, x] = 1
        previous = current


def simulate_sand(grid):
    num_grains = 0
    quit = False
    while not quit:
        x, y = (200, 0)
        while True:
            if y + 1 >= 200:
                quit = True
                break
            if grid[y + 1, x] == 0:
                y += 1
                continue
            if grid[y + 1, x - 1] == 0:
                y += 1
                x -= 1
                continue
            if grid[y + 1, x + 1] == 0:
                y += 1
                x += 1
                continue
            num_grains += 1
            grid[y, x] = 2
            if y == 0:
                quit = True
            break
    return num_grains

def read_grid():
    grid = np.zeros((200, 400))
    with open("input", encoding="utf8") as data:
        for line in data:
            draw_segments(grid, line)
    return grid


def main():
    print("Day 14")
    print("Part 1")
    grid = read_grid()
    res = simulate_sand(grid)
    print(res)

    print("Part 2")
    grid = read_grid()
    y_max = max(np.nonzero(grid)[0])
    for x in range(0, grid.shape[1]):
        grid[y_max + 2, x] = 1
    res = simulate_sand(grid)
    print(res)

    # pyplot.imshow(grid)
    # pyplot.show()



if __name__ == "__main__":
    main()
