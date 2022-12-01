package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"

	"github.com/azebell/advent-of-code/go/aoc"
)

func main() {
	inputStr := aoc.RunSolver(part1, part2)
	fmt.Println(inputStr)
}

func part1(input string) string {
	elfCalories := make([]int, 0)
	input = strings.TrimSpace(input)
	elves := strings.Split(input, "\n\n")
	for _, elf := range elves {
		total := 0
		for _, calories := range strings.Split(elf, "\n") {
			x, err := strconv.Atoi(calories)
			if err != nil {
				panic(err)
			}
			total += x
		}
		elfCalories = append(elfCalories, total)
	}

	max := elfCalories[0]
	for _, v := range elfCalories {
		if v > max {
			max = v
		}
	}

	return fmt.Sprint(max)
}

func part2(input string) string {
	elfCalories := make([]int, 0)
	input = strings.TrimSpace(input)
	elves := strings.Split(input, "\n\n")
	for _, elf := range elves {
		total := 0
		for _, calories := range strings.Split(elf, "\n") {
			x, err := strconv.Atoi(calories)
			if err != nil {
				panic(err)
			}
			total += x
		}
		elfCalories = append(elfCalories, total)
	}

	sort.Slice(elfCalories, func(i, j int) bool {
		return elfCalories[i] > elfCalories[j]
	})

	total := 0
	for _, v := range elfCalories[:3] {
		total += v
	}
	return fmt.Sprint(total)
}
