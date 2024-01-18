package main

import (
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	fileTextBytes, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal("Error when opening input file")
	}

	fileText := string(fileTextBytes)
	fileLines := strings.Split(fileText, "\n")
	totalDelta := 0
	for _, line := range fileLines {
		rawLength := len(line)
		unquoted, err := strconv.Unquote(line)
		if err != nil {
			log.Fatal("Error when unquoting line")
		}
		unquotedLength := len(unquoted)
		delta := rawLength - unquotedLength
		log.Printf("Line: %s: %d", line, delta)
		totalDelta += delta
	}
	log.Printf("Total delta: %d", totalDelta)

	// Part 2 is literally the oposite
	totalDelta = 0
	for _, line := range fileLines {
		quoted := strconv.Quote(line)
		rawLength := len(line)
		quotedLength := len(quoted)
		delta := quotedLength - rawLength
		log.Printf("Line: %s: %d", line, delta)
		totalDelta += delta
	}
	log.Printf("Total delta (part 2): %d", totalDelta)
}
