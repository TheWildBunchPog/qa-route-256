package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)
	var numbers [5]float64

	for i := 0; i < 5; i++ {
		sc.Scan()
		number, err := strconv.ParseFloat(sc.Text(), 64)
		if err != nil { panic(err) }
		numbers[i] = number
	}

	for i := 4; i > -1; i-- {
		fmt.Println(numbers[i])
	}
}