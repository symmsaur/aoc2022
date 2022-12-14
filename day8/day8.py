#!/usr/bin/env python3

import numpy as np
import itertools


def mark_visible(array, visible):
    for y in range(array.shape[0]):
        max_height = -1
        for x in range(array.shape[1]):
            if array[y, x] > max_height:
                max_height = array[y, x]
                visible[y, x] = 1
    return visible


def scenic_score(array, start_pos):
    directions = (np.array(t) for t in ((0, 1), (0, -1), (1, 0), (-1, 0)))
    scores = []
    for direction in directions:
        pos = start_pos + direction
        counter = 1
        while True:
            if not (0 <= pos[0] < array.shape[0] and 0 <= pos[1] < array.shape[1]):
                counter -= 1
                break
            if array[tuple(pos)] >= array[tuple(start_pos)]:
                break
            pos += direction
            counter += 1
        scores.append(counter)
    return np.prod(scores)


def main():
    with open("input", encoding="utf-8") as data:
        raw = []
        for line in data.read().splitlines():
            raw.append([])
            row = raw[-1]
            for char in line:
                row.append(int(char))
    array = np.array(raw)
    visible = np.zeros(array.shape)
    for _ in range(4):
        mark_visible(array, visible)
        array = np.rot90(array)
        visible = np.rot90(visible)
    part_one = int(np.sum(visible))
    print(f"Part One: {part_one}")

    scenic_scores = np.zeros(array.shape)
    for y, x in itertools.product(range(array.shape[0]), range(array.shape[1])):
        scenic_scores[y, x] = scenic_score(array, np.array((y, x)))
    part_two = int(np.amax(scenic_scores))
    print(f"Part Two: {part_two}")


if __name__ == "__main__":
    main()
