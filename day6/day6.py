#!/usr/bin/env python3


def index_of_distinct(buf, num_distinct):
    recent_chars = [None] * num_distinct
    for index, char in enumerate(buf):
        recent_chars = recent_chars[1:num_distinct]
        recent_chars.append(char)
        if index >= num_distinct and len(set(recent_chars)) == num_distinct:
            print(recent_chars)
            break
    return index + 1


def main():
    with open("input") as data:
        buf = data.read()
    part_one = index_of_distinct(buf, 4)
    print(f"Part One: {part_one}")
    part_two = index_of_distinct(buf, 14)
    print(f"Part One: {part_two}")


if __name__ == "__main__":
    main()
