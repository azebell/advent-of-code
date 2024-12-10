from aoc import run_solver


def part1(input_str: str) -> str:
    disk_map = input_str.strip()
    disk = []
    add_space = False
    id = 0
    for c in disk_map:
        if add_space:
            disk.extend([None]*int(c))
        else:
            disk.extend([id]*int(c))
            id += 1
        add_space = not add_space

    i = 0
    while i < len(disk):
        if disk[i] != None:
            i += 1
            continue
        
        id = disk.pop()
        while id == None:
             id = disk.pop()
        disk[i] = id

        i += 1

    answer = sum(pos * id for pos, id in enumerate(disk))
    return str(answer)

def part2(input_str: str) -> str:
    disk_map = input_str.strip()
    disk = []
    add_space = False
    id = 0
    for c in disk_map:
        if add_space:
            disk.append((None, int(c)))
        else:
            disk.append((id, int(c)))
            id += 1
        add_space = not add_space

    return str("")


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
