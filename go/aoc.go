package aoc

import (
	"fmt"
	"io"
	"os"
	"strconv"
)

func RunSolver(solver1 func(string) string, solver2 func(string) string) string {
	config, err := readConfig()
	if err != nil {
		return fmt.Sprint(err)
	}
	switch config.part {
	case 1:
		return solver1(config.inputStr)
	case 2:
		return solver2(config.inputStr)
	default:
		return fmt.Sprintf("Error: Invalid challenge part '%d'", config.part)
	}
}

type Config struct {
	part     uint
	inputStr string
}

func readConfig() (Config, error) {
	if len(os.Args) < 2 {
		fmt.Println("No challenge part specified")
	}
	val, err := strconv.Atoi(os.Args[1])
	if err != nil {
		return Config{0, ""}, err
	}
	part := uint(val)

	if len(os.Args) > 2 {
		inputFilepath := os.Args[2]
		inputStr, err := readFile(inputFilepath)
		if err != nil {
			return Config{}, err
		}
		return Config{part, inputStr}, nil
	}

	inputStr, err := readStdin()
	if err != nil {
		return Config{}, err
	}
	return Config{part, inputStr}, nil
}

func readFile(filepath string) (string, error) {
	bytes, err := os.ReadFile(filepath)
	return string(bytes), err
}

func readStdin() (string, error) {
	bytes, err := io.ReadAll(os.Stdin)
	return string(bytes), err
}
