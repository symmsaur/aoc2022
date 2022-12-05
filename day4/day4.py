#!/usr/bin/env python3


def parse_ranges(row):
    left, right = row.split(",")

    def parse_range(string):
        start, inclusive_end = string.split("-")
        return range(int(start), int(inclusive_end) + 1)

    return parse_range(left), parse_range(right)


def fully_contains(outer, inner):
    return outer[0] <= inner[0] and outer[-1] >= inner[-1]


def overlaps(lhs, rhs):
    return any(set(lhs).intersection(set(rhs)))

def main():
    with open("input") as data:
        range_pairs = [parse_ranges(row) for row in data.readlines()]
    selected = [
        (l, r)
        for l, r in range_pairs
        if fully_contains(l, r) or fully_contains(r, l)
    ]
    count = len(selected)
    print(f"Part One: {count}")
    selected_overlaps = [
        (l, r)
        for l, r in range_pairs
        if overlaps(l, r)
        ]
    count_overlaps = len(selected_overlaps)
    print(f"Part Two: {count_overlaps}")


if __name__ == "__main__":
    main()
