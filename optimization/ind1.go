package main

import "fmt"

func f(x float64) float64 {
	return x*x - 2*x + 3
}

func fibonacci(n int) int {
	if n <= 1 {
		return n
	}
	return fibonacci(n-1) + fibonacci(n-2)
}

func dihotomoia(a, b float64) float64 {
	eps := 0.2
	l := 0.5
	length := b - a
	var y, z float64
	for float64(length) > l {
		y = (a + b - eps) / 2
		z = (a + b + eps) / 2
		if f(y) <= f(z) {
			b = z
		} else {
			a = y
		}
		length = b - a
	}
	return (a + b) / 2
}

func fibonacciSearch(a0, b0 float64) float64 {
	eps := 0.2
	l := 0.5
	L0 := b0 - a0

	N := 0
	for {
		fib := fibonacci(N)
		if float64(fib) >= L0/l {
			break
		}
		N++
	}
	k := 0
	a := a0
	b := b0
	var y, z float64

	y = a + (float64(fibonacci(N-2))/float64(fibonacci(N)))*(b-a)
	z = a + (float64(fibonacci(N-1))/float64(fibonacci(N)))*(b-a)

	fy := f(y)
	fz := f(z)

	for k < N-3 {
		if fy <= fz {
			b = z
			z = y
			y = a + (float64(fibonacci(N-k-3))/float64(fibonacci(N-k-1)))*(b-a)
			fz = fy
			fy = f(y)
		} else {
			a = y
			y = z
			z = a + (float64(fibonacci(N-k-2))/float64(fibonacci(N-1-k)))*(b-a)
			fy = fz
			fz = f(z)
		}
		k++
	}

	y = (a + b) / 2
	z = y + eps

	fy = f(y)
	fz = f(z)

	if fy <= fz {
		b = z
	} else {
		a = y
	}

	return (a + b) / 2
}

func main() {
	resultDih := dihotomoia(-2, 8)
	resultFib := fibonacciSearch(-2, 8)
	fmt.Println(resultDih, resultFib)
}
