#!/usr/bin/env python3

def main():
    with open("input") as data:
        rows = [line.strip() for line in data.readlines()]

    largest = [0, 0, 0]
    current = 0
    for row in rows:
        if row == "":
            largest.append(current)
            largest = sorted(largest, reverse=True)[:3]
            current = 0
        else:
            current += int(row)
    print(f"Part One: {largest[0]}")
    print(f"Part Two: {sum(largest)}")


if __name__ == "__main__":
    main()
