import numpy as np

def erf(x, n=1000):
    def integrand(t):
        return (2 / np.sqrt(np.pi)) * np.exp(-t**2)
    
    a, b = 0, x 
    h = (b - a) / n
    integral = 0.5 * (integrand(a) + integrand(b))
    for i in range(1, n):
        integral += integrand(a + i * h)
    return h * integral

def equation(x):
    return erf(x) - 0.5

def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        f_x0, f_x1 = f(x0), f(x1)
        if abs(f_x1) < tol:
            return x1
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x2
        if abs(x1 - x0) < tol:
            return x1
    raise RuntimeError("Метод секущих не сошелся за заданное число итераций")

x0, x1 = 0, 1 
root = secant_method(equation, x0, x1)

print(f"Значение x, при котором erf(x) = 0.5: {root:.6f}")
