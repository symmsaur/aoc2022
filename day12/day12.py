#!/usr/bin/env python3

import queue


def neighbors(pos, dims):
    return set(
        p
        for p in (
            (pos[0] + 1, pos[1]),
            (pos[0] - 1, pos[1]),
            (pos[0], pos[1] + 1),
            (pos[0], pos[1] - 1),
        )
        if 0 <= p[0] < dims[0] and 0 <= p[1] < dims[1]
    )


def dijkstra_dist(start, goals, check, dims):
    visited = set()
    pending = queue.PriorityQueue()
    pending.put((0, start))
    distances = []
    while not pending.empty():
        dist, cur = pending.get()
        cur_neighbors = neighbors(cur, dims) - visited
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
    dims = (len(rows[0]), len(rows))

    def level(pos):
        return rows[pos[1]][pos[0]]

    part_one = dijkstra_dist(
        start, (goal,), lambda cur, to: level(to) - level(cur) <= 1, dims
    )[0]
    print(f"Part One: {part_one}")
    candidate_starts = []
    for y, cols in enumerate(rows):
        for x, c in enumerate(cols):
            if c == ord("a"):
                candidate_starts.append((x, y))
    part_two = min(
        dijkstra_dist(
            goal,
            candidate_starts,
            lambda cur, to: level(cur) - level(to) <= 1,
            dims,
        )
    )
    print(f"Part Two: {part_two}")


if __name__ == "__main__":
    main()
