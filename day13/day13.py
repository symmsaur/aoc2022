#!/usr/bin/env python3

import ast
import functools


def compare(lhs, rhs):
    if isinstance(lhs, int) and isinstance(rhs, int):
        if lhs < rhs:
            return -1
        if lhs > rhs:
            return 1
        return 0
    if isinstance(lhs, int):
        lhs = [lhs]
    if isinstance(rhs, int):
        rhs = [rhs]
    for l_inner, r_inner in zip(lhs, rhs):
        if (res := compare(l_inner, r_inner)) != 0:
            return res
    if len(lhs) < len(rhs):
        return -1
    if len(lhs) > len(rhs):
        return 1
    return 0


def main():
    with open("input", encoding="utf8") as data:
        lines = [ast.literal_eval(l) for l in data if not l == "\n"]
    part_one = sum(
        index
        for index, (lhs, rhs) in enumerate(zip(lines[:-1:2], lines[1::2]), 1)
        if compare(lhs, rhs) == -1
    )
    print(f"Part One: {part_one}")
    ordered = sorted(lines + [[[2]], [[6]]], key=functools.cmp_to_key(compare))
    part_two = (ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1)
    print(f"Part Two: {part_two}")


if __name__ == "__main__":
    main()
