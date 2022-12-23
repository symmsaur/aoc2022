#!/usr/bin/env python3


def parse_op(op_str):
    if op_str == "old * old":
        return lambda x: x * x
    else:
        parts = op_str.split()
        if parts[1] == "+":
            return lambda x: x + int(parts[2])
        elif parts[1] == "*":
            return lambda x: x * int(parts[2])
        else:
            raise ValueError(f"Unexpected op in {parts}")


class Monkey:
    def __init__(self, lines):
        self.items = [int(i) for i in lines[1].split(":")[1].split(",")]
        self.operation = parse_op(lines[2].split("=")[1].strip())
        self.test = int(lines[3].split()[-1])
        self.dest_true = int(lines[4].split()[-1])
        self.dest_false = int(lines[5].split()[-1])
        self.business = 0

    def __repr__(self):
        return f"Monkey( items={self.items} test={self.test} true={self.dest_true} false={self.dest_false} )"


def main():
    with open("input", encoding="utf8") as data:
        monkeys = []
        lines = []
        for line in [l.strip() for l in data]:
            if line == "":
                monkeys.append(Monkey(lines))
                lines = []
            else:
                lines.append(line)
        monkeys.append(Monkey(lines))
        lines = []
    for _ in range(20):
        for monkey in monkeys:
            print(monkey)
            while monkey.items:
                monkey.business += 1
                worry = monkey.operation(monkey.items[0]) // 3
                monkey.items = monkey.items[1:]
                if not worry % monkey.test:
                    monkeys[monkey.dest_true].items.append(worry)
                else:
                    monkeys[monkey.dest_false].items.append(worry)
    business = sorted([m.business for m in monkeys])
    part_one = business[-1] * business[-2]
    print(f"Part One: {part_one}")


if __name__ == "__main__":
    main()
