from aoc import run_solver
import os


def part1(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    dir_sizes, subdirs = process_folders(lines)

    total = 0
    for dir in dir_sizes:
        size = get_size(dir, dir_sizes, subdirs)
        if size <= 100000:
            total += size

    return str(total)


def part2(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    dir_sizes, subdirs = process_folders(lines)

    space = 70000000
    used = get_size("/", dir_sizes, subdirs)
    min_delete = used
    for dir in dir_sizes:
        freed_space = get_size(dir, dir_sizes, subdirs)
        unused = space - used + freed_space
        if unused >= 30000000:
            min_delete = min(min_delete, freed_space)

    return str(min_delete)


def process_folders(lines: list[str]):
    curr = "/"
    dir_sizes = {"/": 0}
    subdirs = {"/": []}

    for line in lines:
        match line.split():
            case ["$", "cd", "/"]:
                curr = "/"
            case ["$", "cd", dest]:
                curr = os.path.normpath(os.path.join(curr, dest))
                if curr not in dir_sizes:
                    dir_sizes[curr] = 0
                    subdirs[curr] = []
            case ["$", _]:
                pass
            case ["dir", name]:
                subdirs[curr].append(os.path.normpath(os.path.join(curr, name)))
            case [size, name]:
                dir_sizes[curr] += int(size)

    return dir_sizes, subdirs


def get_size(dirname, dir_sizes, subdirs) -> int:
    size = dir_sizes[dirname]
    for subdir in subdirs[dirname]:
        if subdir in dir_sizes:
            size += get_size(subdir, dir_sizes, subdirs)
    return size


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
