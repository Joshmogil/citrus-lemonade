package main

import (
	"fmt"
)

func decimalToBinary(numer int) int {
	var rStore []int

	for (numer>0) {
		rStore = append(rStore, (numer % 2))
		numer = numer / 2
	}
	return rStore[0]
}

func main(){
	var input int
	fmt.Scanln(&input)
	th := decimalToBinary(input)
	fmt.Printf("%d",th)
}