#!/usr/bin/env python3

import queue


def level(rows, pos):
    if not 0 <= pos[0] < len(rows[0]):
        return 1000
    if not 0 <= pos[1] < len(rows):
        return 1000
    return rows[pos[1]][pos[0]]


def neighbors(pos):
    return {
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
    }


def dijkstra_dist(start, goals, check):
    visited = set()
    pending = queue.PriorityQueue()
    pending.put((0, start))
    distances = []
    while not pending.empty():
        dist, cur = pending.get()
        cur_neighbors = neighbors(cur) - visited
        for neighbor in cur_neighbors:
            if check(cur, neighbor):
                if neighbor in goals:
                    distances.append(dist + 1)
                pending.put((dist + 1, neighbor))
                visited.add(neighbor)
    return distances


def main():
    with open("input", encoding="utf8") as data:
        rows = []
        for y, line in enumerate((l.strip() for l in data)):
            cols = []
            for x, l in enumerate((ord(c) for c in line)):
                if l == ord("S"):
                    start = x, y
                    cols.append(ord("a"))
                elif l == ord("E"):
                    goal = x, y
                    cols.append(ord("z"))
                else:
                    cols.append(l)
            rows.append(cols)

    def can_step_up(cur, neighbor):
        return level(rows, neighbor) - level(rows, cur) <= 1

    part_one = dijkstra_dist(start, (goal,), can_step_up)[0]
    print(f"Part One: {part_one}")
    candidate_starts = []
    for y, cols in enumerate(rows):
        for x, c in enumerate(cols):
            if c == ord("a"):
                candidate_starts.append((x, y))

    def can_step_down(cur, neighbor):
        if level(rows, neighbor) == 1000:
            return False
        return level(rows, cur) - level(rows, neighbor) <= 1

    part_two = min(dijkstra_dist(goal, candidate_starts, can_step_down))
    print(f"Part Two: {part_two}")


if __name__ == "__main__":
    main()
