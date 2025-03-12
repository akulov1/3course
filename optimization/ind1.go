package main

import (
	"fmt"
	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/vg"
	"math"
)

func f(x float64) float64 {
	return x*x - 2*x + 3
}

func dihotomoia(a, b float64) float64 {
	eps := 0.2
	l := 0.5
	length := b - a
	var y, z float64
	k := 0
	for float64(length) > l {
		y = (a + b - eps) / 2
		z = (a + b + eps) / 2
		if f(y) <= f(z) {
			b = z
		} else {
			a = y
		}
		length = b - a
		k++
	}
	fmt.Println("K =", k, " N = ", 2*k)
	fmt.Println("R(N) =", 1/math.Pow(2, float64(k)))
	fmt.Printf("[%f,%f]\n", a, b)
	res := (a + b) / 2
	fmt.Println("x* =", res, "f(x*) =", f(res))
	return (a + b) / 2
}

func fibonacci(n int) int {
	if n <= 1 {
		return n
	}
	return fibonacci(n-1) + fibonacci(n-2)
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
	fmt.Println("K =", k, " N =", N)
	fmt.Println("R(N) =", 1/float64(fibonacci(N)))
	fmt.Printf("[%f,%f]\n", a, b)
	res := (a + b) / 2
	fmt.Println("x* =", res, "f(x*) =", f(res))
	return (a + b) / 2
}

func goldenSection(a0, b0 float64) {
	k := 0
	y0 := a0 + (3-math.Sqrt(5))/2*(b0-a0)
	z0 := a0 + b0 - y0
	length := b0 - a0
	for length > 0.5 {
		fy := f(y0)
		fz := f(z0)
		if fy <= fz {
			b0 = z0
			z0 = y0
			y0 = a0 + b0 - y0
		} else {
			a0 = y0
			y0 = z0
			z0 = a0 + b0 - z0
		}
		k++
		length = b0 - a0
	}
	N := k + 2
	RN := math.Pow(0.618, float64(N-1))
	fmt.Println("K =", k, " N =", N)
	fmt.Println("R(N) =", RN)
	fmt.Printf("[%f,%f]\n", a0, b0)
	res := (a0 + b0) / 2
	fmt.Println("x* =", res, "f(x*) =", f(res))
}

func main() {
	fmt.Println("Метод дихотомии")
	dihotomoia(-2, 8)
	fmt.Println("Метод Фибоначчи")
	fibonacciSearch(-2, 8)
	fmt.Println("Метод золотого сечения")
	goldenSection(-2, 8)
	p := plot.New()
	p.Title.Text = "График функции"
	p.X.Label.Text = "x"
	p.Y.Label.Text = "f(x)"

	xMin, xMax := -2.0, 8.0
	numPoints := 100

	points := make(plotter.XYs, numPoints)
	for i := 0; i < numPoints; i++ {
		x := xMin + float64(i)*(xMax-xMin)/float64(numPoints-1)
		points[i].X = x
		points[i].Y = f(x)
	}

	line, err := plotter.NewLine(points)
	if err != nil {
		fmt.Println("Ошибка при создании графика:", err)
		return
	}
	p.Add(line)

	p.X.Min = xMin
	p.X.Max = xMax

	if err := p.Save(8*vg.Inch, 4*vg.Inch, "plot.png"); err != nil {
		fmt.Println("Ошибка сохранения:", err)
	}
}
