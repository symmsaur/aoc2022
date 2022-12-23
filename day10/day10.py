#!/usr/bin/env python3


def main():
    with open("input", encoding="utf8") as data:
        program = [l.strip().split() for l in data]
    cycle = 1
    x_reg = 1
    interesting_cycles = list(range(20, 221, 40))
    total_signal_strength = 0
    x = 0
    for instruction in program:
        old_x_reg = x_reg
        old_cycle = cycle
        if instruction[0] == "noop":
            cycle += 1
        elif instruction[0] == "addx":
            x_reg += int(instruction[1])
            cycle += 2
        # Part One
        if interesting_cycles and cycle > interesting_cycles[0]:
            total_signal_strength += interesting_cycles[0] * old_x_reg
            interesting_cycles = interesting_cycles[1:]
        # Part Two
        for _ in range(cycle - old_cycle):
            if abs(x - old_x_reg) < 2:
                print("#", end="")
            else:
                print(" ", end="")
            x += 1
            if x > 39:
                x = 0
                print()
    print(f"Part One: {total_signal_strength}")


if __name__ == "__main__":
    main()
