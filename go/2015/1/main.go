package main

import (
	"fmt"

	"github.com/azebell/advent-of-code/go/aoc"
)

func main() {
	inputStr := aoc.RunSolver(part1, part2)
	fmt.Println(inputStr)
}

func part1(input string) string {
	floor := 0
	for _, c := range input {
		if c == '(' {
			floor += 1
		} else if c == ')' {
			floor -= 1
		}
	}
	return fmt.Sprint(floor)
}

func part2(input string) string {
	floor := 0
	position := 1
	for _, c := range input {
		if c == '(' {
			floor += 1
		} else if c == ')' {
			floor -= 1
		}
		if floor < 0 {
			break
		}
		position += 1
	}
	return fmt.Sprint(position)
}
