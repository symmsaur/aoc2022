#!/usr/bin/env python3

import numpy as np


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tup(self):
        return (self.x, self.y)


def compute_visited(moves, snake_length):
    snake = [Pos(0, 0) for _ in range(snake_length)]
    visited = set()
    for move in moves:
        for _ in range(move[1]):
            if move[0] == "U":
                snake[0].y += 1
            elif move[0] == "R":
                snake[0].x += 1
            elif move[0] == "D":
                snake[0].y -= 1
            elif move[0] == "L":
                snake[0].x -= 1
            for h, t in zip(snake[:-1], snake[1:]):
                if abs(t.x - h.x) + abs(t.y - h.y) >= 3:  # diagonal
                    t.x += np.sign(h.x - t.x)
                    t.y += np.sign(h.y - t.y)
                else:
                    if abs(t.x - h.x) >= 2:
                        t.x += np.sign(h.x - t.x)
                    elif abs(t.y - h.y) >= 2:
                        t.y += np.sign(h.y - t.y)
            visited.add(snake[-1].tup())
    return visited


def main():
    with open("input", encoding="utf8") as data:
        moves = [l.strip().split() for l in data]
        moves = [(m[0], int(m[1])) for m in moves]
    visited_part_one = compute_visited(moves, 2)
    part_one = len(visited_part_one)
    print(f"Part One: {part_one}")
    visited_part_two = compute_visited(moves, 10)
    part_two = len(visited_part_two)
    print(f"Part One: {part_two}")


if __name__ == "__main__":
    main()
