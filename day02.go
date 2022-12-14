package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	var inputFile = flag.String("inputFile", "inputs/day02.txt", "Relative file path to use as input")

	flag.Parse()

	bytes, err := os.ReadFile(*inputFile)

	if err != nil {
		log.Fatal(err)
	}

	contents := string(bytes)
	data := strings.Split(contents, "\n")
	score := 0

	// first
	for _, s := range data {
		if s == "" {
			break
		}

		vals := strings.Split(s, " ")
		score += getScore(vals)
	}

	fmt.Println(score)

	score = 0

	// second
	//  A for Rock, B for Paper, and C for Scissors
	for _, s := range data {
		if s == "" {
			break
		}

		vals := replace(strings.Split(s, " "))
		score += getScore(vals)
	}

	fmt.Println(score)
}

func getScore(vals []string) int {
	score := 0
	if vals[1] == "X" { // Rock
		if vals[0] == "C" {
			score += 6
		} else if vals[0] == "A" {
			score += 3
		}
		score += 1
	}

	if vals[1] == "Y" { // Paper
		if vals[0] == "A" {
			score += 6
		} else if vals[0] == "B" {
			score += 3
		}
		score += 2
	}

	if vals[1] == "Z" { // Scissors
		if vals[0] == "B" {
			score += 6
		} else if vals[0] == "C" {
			score += 3
		}
		score += 3
	}
	return score
}

func replace(vals []string) []string {
	if vals[1] == "X" {
		if vals[0] == "A" {
			vals[1] = "Z"
		}
		if vals[0] == "B" {
			vals[1] = "X"
		}
		if vals[0] == "C" {
			vals[1] = "Y"
		}
	} else if vals[1] == "Y" {
		if vals[0] == "A" {
			vals[1] = "X"
		}
		if vals[0] == "B" {
			vals[1] = "Y"
		}
		if vals[0] == "C" {
			vals[1] = "Z"
		}
	} else {
		if vals[0] == "A" {
			vals[1] = "Y"
		}
		if vals[0] == "B" {
			vals[1] = "Z"
		}
		if vals[0] == "C" {
			vals[1] = "X"
		}
	}
	return vals
}
