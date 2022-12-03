#!/usr/bin/env python3

def prio_score(item_val):
    if 65 <= item_val <= 90:
        return item_val - 65 + 27
    else:
        # ord('a') == 97
        return item_val - 96


def priority(rucksack):
    first = set(rucksack[:len(rucksack)//2])
    second = set(rucksack[len(rucksack)//2:])
    items = first.intersection(second)
    assert len(items) == 1
    item_val = ord(items.pop())
    return prio_score(item_val)


def common_item(rucksacks):
    sets = [set(r) for r in rucksacks]
    common_items = sets[0]
    for s in sets[1:]:
        common_items = common_items.intersection(s)
    assert len(common_items) == 1
    item_val = ord(common_items.pop())
    return prio_score(item_val)


def partition_by_three(in_list):
    output = []
    for item in in_list:
        output.append(item)
        if len(output) == 3:
            yield output
            output = []


def main():
    with open("input") as data:
        rucksacks = [line.strip() for line in data.readlines()]
    priorities = [priority(rucksack) for rucksack in rucksacks]
    total = sum(priorities)
    print(f"Part One: {total}")
    badge_prios = [common_item(r) for r in partition_by_three(rucksacks)]
    badge_total = sum(badge_prios)
    print(f"Part Two: {badge_total}")


if __name__ == "__main__":
    main()
