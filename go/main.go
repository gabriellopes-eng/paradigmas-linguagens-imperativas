package main

import (
	"fmt"
	"math/rand"
	"os"
	"time"

	"paradigmas-go/hanoi"
	"paradigmas-go/knapsack"
	"paradigmas-go/sorting"
)

func countLines(path string) int {

	content, _ := os.ReadFile(path)

	lines := 0

	for _, char := range content {

		if char == '\n' {
			lines++
		}
	}

	return lines
}

func fileSize(path string) float64 {

	info, _ := os.Stat(path)

	return float64(info.Size()) / 1024
}

func main() {

	// QUICKSORT
	numbers := rand.Perm(50000)

	start := time.Now()

	sorting.QuickSort(numbers)

	quicksortTime :=
		time.Since(start).Seconds()

	// HANOI
	var moves []string

	start = time.Now()

	hanoi.Solve(
		20,
		"A",
		"B",
		"C",
		&moves,
	)

	hanoiTime :=
		time.Since(start).Seconds()

	// KNAPSACK
	weights := []int{
		2, 5, 7, 3, 1,
		4, 6, 8, 9, 2,
	}

	values := []int{
		10, 4, 8, 5, 3,
		7, 6, 9, 2, 1,
	}

	for i := 0; i < 10000; i++ {

		knapsack.Solve(
			20,
			weights,
			values,
		)
	}

	knapsackTime :=
		time.Since(start).Seconds()

	// METRICS TABLE
	fmt.Println("\n==============================================================")
	fmt.Println("COMPARATIVE METRICS - GO")
	fmt.Println("==============================================================")

	fmt.Printf(
		"%-20s%-15s%-10s%-15s\n",
		"Problem",
		"Time(s)",
		"Lines",
		"Size(KB)",
	)

	fmt.Println("------------------------------------------------------------")

	fmt.Printf(
		"%-20s%-15f%-10d%-15.2f\n",
		"QuickSort",
		quicksortTime,
		countLines("sorting/sorting.go"),
		fileSize("sorting/sorting.go"),
	)

	fmt.Printf(
		"%-20s%-15f%-10d%-15.2f\n",
		"Towers of Hanoi",
		hanoiTime,
		countLines("hanoi/hanoi.go"),
		fileSize("hanoi/hanoi.go"),
	)

	fmt.Printf(
		"%-20s%-15f%-10d%-15.2f\n",
		"Knapsack",
		knapsackTime,
		countLines("knapsack/knapsack.go"),
		fileSize("knapsack/knapsack.go"),
	)

	fmt.Println("==============================================================")
}
