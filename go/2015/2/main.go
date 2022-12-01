package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"

	"github.com/azebell/advent-of-code/go/aoc"
)

func main() {
	inputStr := aoc.RunSolver(part1, part2)
	fmt.Println(inputStr)
}

func part1(input string) string {
	paper := 0
	input = strings.TrimSpace(input)
	for _, line := range strings.Split(input, "\n") {
		dimensions := strings.Split(line, "x")
		l, _ := strconv.Atoi(dimensions[0])
		w, _ := strconv.Atoi(dimensions[1])
		h, _ := strconv.Atoi(dimensions[2])

		surface := 2*l*w + 2*w*h + 2*h*l
		slack := int(math.Min(float64(l*w), math.Min(float64(w*h), float64(h*l))))
		paper += surface + slack
	}
	return fmt.Sprint(paper)
}

func part2(input string) string {
	ribbon := 0
	input = strings.TrimSpace(input)
	for _, line := range strings.Split(input, "\n") {
		dimensions := strings.Split(line, "x")
		l, _ := strconv.Atoi(dimensions[0])
		w, _ := strconv.Atoi(dimensions[1])
		h, _ := strconv.Atoi(dimensions[2])

		biggest := int(math.Max(float64(l), math.Max(float64(w), float64(h))))
		ab := l + w + h - biggest

		wrap := 2 * ab
		bow := l * w * h
		ribbon += wrap + bow
	}
	return fmt.Sprint(ribbon)
}
