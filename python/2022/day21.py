from aoc import run_solver


def part1(input_str: str) -> str:
    expression_tree = {}

    for line in input_str.strip().splitlines():
        monkey, expression = line.split(": ")
        expression_tree[monkey] = expression.split()

    def postorder(key):
        current = expression_tree[key]
        match current:
            case [left, op, right]:
                left = postorder(left)
                right = postorder(right)
                return eval(f"left {op} right")
            case [number]:
                return int(number)

    answer = postorder("root")

    return str(answer)


def part2(input_str: str) -> str:
    expression_tree = {}

    for line in input_str.strip().splitlines():
        monkey, expression = line.split(": ")
        expression_tree[monkey] = expression.split()

    expression_tree["humn"] = [1j]

    def postorder(key):
        current = expression_tree[key]
        match current:
            case [left, op, right]:
                left = postorder(left)
                right = postorder(right)
                return eval(f"left {op} right")
            case [number]:
                return complex(number)

    left, _, right = expression_tree["root"]
    left = postorder(left)
    right = postorder(right)

    answer = (right - left.real) / left.imag
    answer = round(answer.real)

    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
