package main

import (
	"fmt"
)

type Fraction struct {
	numerator int;
	denominator int; 
	}


func gcd(u int, v int) int {
    //60 80
	var t int;
	for (u>0) {
		
		if (u < v) {
			t = u; //t=60 20
			u = v; //u=80 60
			v = t; 
		}
		      
        u = u - v; 
		
	}
    return v;
    }

func simplify(fr Fraction) Fraction{
    comdom := gcd(fr.numerator,fr.denominator);
	
    fr.numerator = fr.numerator/comdom;
	fmt.Printf("%d/%d \n",fr.denominator,comdom)
    fr.denominator = fr.denominator/comdom;
	fmt.Printf("%d/%d \n",fr.denominator, fr.numerator)
	
    return fr;
}

func main() {
        var numerator int
		fmt.Scanln(&numerator)
		var denominator int
		fmt.Scanln(&denominator)
		
		fract := Fraction{numerator: numerator, denominator: denominator}
		
		fr := simplify(fract)


		fmt.Printf("%d/%d -> %d/%d \n",numerator,denominator,fr.numerator,fr.denominator)

                
    }