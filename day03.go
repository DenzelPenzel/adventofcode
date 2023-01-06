package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	var inputFile = flag.String("inputFile", "inputs/day03.txt", "Relative file path to use as input")

	flag.Parse()

	bytes, err := os.ReadFile(*inputFile)

	if err != nil {
		log.Fatal(err)
	}

	contents := string(bytes)
	data := strings.Split(contents, "\n")
	var res int

	for _, s := range data {
		if s == "" {
			break
		}
		mapping := make(map[rune]bool)
		mid := len(s) / 2

		for _, c := range s[:mid] {
			mapping[c] = true
		}

		for _, c := range s[mid:] {
			if mapping[c] {
				if c >= 'a' && c <= 'z' {
					res += int(c-'a') + 1
				} else {
					res += int(c-'A') + 27
				}
				break
			}
		}

	}

	fmt.Println(res)

	res = 0

	for i := 0; i < len(data); i += 3 {
		m1 := make(map[rune]bool)
		m2 := make(map[rune]bool)
		m3 := make(map[rune]bool)

		for k := 0; k < 3; k++ {
			for _, v := range data[i+k] {
				if k == 0 {
					m1[v] = true
				} else if k == 1 {
					m2[v] = true
				} else {
					m3[v] = true
				}
			}
		}

		for _, c := range data[i] {
			if m1[c] && m2[c] && m3[c] {
				if c >= 'a' && c <= 'z' {
					res += int(c-'a') + 1
				} else {
					res += int(c-'A') + 27
				}
				break
			}
		}
	}

	fmt.Println(res)

	xx := make(map[int]bool, 10)

	for i := 0; i < 10; i++ {
		xx[i] = true
	}

	rms := []int{}

	fmt.Println(xx)

	for k := range xx {
		rms = append(rms, k)
	}

	fmt.Println(rms)

}
