package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	var inputFile = flag.String("inputFile", "inputs/day01.txt", "Relative file path to use as input")

	flag.Parse()

	bytes, err := os.ReadFile(*inputFile)

	if err != nil {
		log.Fatal(err)
	}

	contents := string(bytes)
	data := strings.Split(contents, "\n")

	var current int
	var maxValue int

	for _, s := range data {
		if s == "" {
			if maxValue < current {
				maxValue = current
			}
			current = 0
		}
		num, _ := strconv.Atoi(s)
		current += num
	}

	if maxValue < current {
		maxValue = current
	}

	fmt.Println(maxValue)

	current = 0
	var maxSums []int

	for _, s := range data {
		if s == "" {
			maxSums = append(maxSums, current)
			current = 0
		}

		num, _ := strconv.Atoi(s)
		current += num
	}

	maxSums = append(maxSums, current)
	total := 0
	sort.Ints(maxSums)

	for i := 1; i <= 3; i++ {
		total += maxSums[len(maxSums)-i]
	}

	fmt.Println(total)

}
