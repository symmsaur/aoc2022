#!/usr/bin/env python3

from pprint import pprint
import re


def parse_stacks(lines):
    # There are 9 stacks
    # [D] [V] [W] [R] [M] [G] [R] [N] [D]
    # 0123456789
    #  |<->|
    #    4
    stacks = [[] for _ in range(9)]
    for line in lines[:-1]:
        for i in range(9):
            pos = 4 * i + 1
            if line[pos] != " ":
                stacks[i].append(line[pos])
    for stack in stacks:
        stack.reverse()
    return stacks


def parse_program(lines):
    pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")
    program = []
    for line in lines:
        match = pattern.match(line)
        groups = match.groups()
        program.append(
            {
                "num": int(groups[0]),
                "src": int(groups[1]) - 1,
                "dest": int(groups[2]) - 1,
            }
        )
    return program


def parse(lines):
    separation_point = lines.index("\n")
    stacks = parse_stacks(lines[:separation_point])
    program = parse_program(lines[separation_point + 1 :])
    return stacks, program


def run(stacks, program):
    for instruction in program:
        for _ in range(instruction["num"]):
            stacks[instruction["dest"]].append(stacks[instruction["src"]].pop())

def run2(stacks, program):
    for instruction in program:
        stacks[instruction["dest"]].extend(stacks[instruction["src"]][-instruction["num"]:])
        stacks[instruction["src"]] = stacks[instruction["src"]][:-instruction["num"]]

def part1():
    with open("input") as data:
        stacks, program = parse([l for l in data.readlines()])
    run(stacks, program)
    part_one_result = "".join([s[-1] for s in stacks])
    print(f"Part One: {part_one_result}")

def part2():
    with open("input") as data:
        stacks, program = parse([l for l in data.readlines()])
    run2(stacks, program)
    part_two_result = "".join([s[-1] for s in stacks])
    print(f"Part Two: {part_two_result}")

def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
