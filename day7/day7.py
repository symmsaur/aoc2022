#!/usr/bin/env python3
from collections import namedtuple

File = namedtuple("File", ["name", "size"])


class Dir:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.children = []
        self._total_size = None

    def add_child(self, name):
        child = Dir(self, name)
        self.children.append(child)
        return child

    def add_file(self, name, size):
        self.children.append(File(name, size))

    def recurse(self, include_files=True):
        yield self
        for child in self.children:
            if include_files and isinstance(child, File):
                yield child
            elif isinstance(child, Dir):
                yield from child.recurse(include_files)

    def total_size(self):
        if self._total_size:
            return self._total_size
        total_size = 0
        for child in self.children:
            if isinstance(child, File):
                total_size += child.size
            else:
                total_size += child.total_size()
        self._total_size = total_size
        return self._total_size


def parse_fs(data):
    current = Dir(None, "/")
    root = current
    for line in [l.strip() for l in data]:
        if line == "$ cd /":
            current = root
        elif line == "$ cd ..":
            current = current.parent
        elif line.startswith("$ cd"):
            current = current.add_child(line.split()[-1])
        elif line.split()[0].isdigit():
            size, name = line.split()
            current.add_file(name, int(size))
    return root


def main():
    with open("input", encoding="utf-8") as data:
        filesystem = parse_fs(data)

    selected_dirs = [
        d for d in filesystem.recurse(include_files=False) if d.total_size() <= 100000
    ]
    sizes = [d.total_size() for d in selected_dirs]
    part_one = sum(sizes)
    print(f"Part One: {part_one}")

    free = 70000000 - filesystem.total_size()
    space_to_free = 30000000 - free
    candidates = sorted(
        [
            d
            for d in filesystem.recurse(include_files=False)
            if d.total_size() >= space_to_free
        ],
        key=lambda d: d.total_size(),
    )
    part_two = candidates[0].total_size()
    print(f"Part Two: {part_two}")


if __name__ == "__main__":
    main()
