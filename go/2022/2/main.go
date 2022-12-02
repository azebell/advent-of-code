package main

import (
	"fmt"
	"strings"

	"github.com/azebell/advent-of-code/go/aoc"
)

func main() {
	inputStr := aoc.RunSolver(part1, part2)
	fmt.Println(inputStr)
}

func part1(input string) string {
	input = strings.TrimSpace(input)
	lines := strings.Split(input, "\n")
	shapePoints := [3]int{1, 2, 3}
	points := 0
	for _, line := range lines {
		p := int(line[0] - 'A')
		q := int(line[2] - 'X')

		points += shapePoints[q]
		switch q - p {
		case 1, -2:
			points += 6
		case 0:
			points += 3
		}
	}

	return fmt.Sprint(points)
}

func part2(input string) string {
	input = strings.TrimSpace(input)
	lines := strings.Split(input, "\n")
	shapePoints := [3]int{1, 2, 3}
	points := 0
	for _, line := range lines {
		p := int(line[0] - 'A')
		q := int(line[2] - 'X')

		points += q * 3
		offset := 0
		switch q {
		case 0: // should lose
			offset = -1
		case 1: // should draw
			offset = 0
		case 2: // should win
			offset = 1
		}
		shape := modulo(p+offset, 3)
		points += shapePoints[shape]
	}

	return fmt.Sprint(points)
}

func modulo(a, b int) int {
	return (a%b + b) % b
}
