import sys
from dataclasses import dataclass
from typing import Callable


def run_solver(solver1: Callable[[str], str], solver2: Callable[[str], str]) -> str:
    config = read_config()
    match config.part:
        case 1:
            return solver1(config.input_str)
        case 2:
            return solver2(config.input_str)
        case 0:
            return "\n".join([solver1(config.input_str), solver2(config.input_str)])
        case _:
            return f"Error: Invalid challenge part '{config.part}'"


@dataclass
class Config:
    part: int
    input_str: str


def read_config() -> Config:
    if len(sys.argv) < 2:
        print("No challenge part specified")
        sys.exit(1)
    part = int(sys.argv[1])
    if len(sys.argv) > 2:
        input_filepath = sys.argv[2]
        input_str = read_file(input_filepath)
        return Config(part, input_str)
    return Config(part, read_stdin())


def read_stdin() -> str:
    return sys.stdin.read()


def read_file(filepath: str) -> str:
    with open(filepath, "r") as f:
        content = f.read()
    return content
