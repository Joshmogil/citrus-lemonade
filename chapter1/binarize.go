package main

import (
	"fmt"
	"strings"
)

func arrayToString(a []int, delim string) string {
	return strings.Trim(strings.Replace(fmt.Sprint(a)," ", delim, -1), "[]")
} 

func decimalToBinary(numer int) string {
	var rStore []int

	for (numer>0) {
		remain := numer % 2
		rStore = append(rStore, remain)
		numer = numer / 2
		fmt.Printf("%d , remainder %d\n", numer, remain)
	}

	for i, j := 0, len(rStore) -1; i < j; i, j = i+1, j-1 {
		rStore[i], rStore[j] = rStore[j], rStore[i]
	}

	return arrayToString(rStore,"")
}

func main(){
	var input int
	fmt.Scanln(&input)
	th := decimalToBinary(input)
	fmt.Printf("%s",th)
}