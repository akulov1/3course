def phi(x, tol=5e-8):
    sum_phi = 0
    k = 1
    term = 1 / (k * (k + x))
    while abs(term) > tol:
        sum_phi += term
        k += 1
        term = 1 / (k * (k + x))
    return sum_phi


x_values = [i * 0.1 for i in range(11)]
for x in x_values:
    print(f'phi({str(x)[:3]}) = {phi(x)}')

print()
print(f'ряд, который сходится быстрее: 1-x / k*(k+x)*(k+1)')
print()

def s(x, error=3e-8):
    sum_s = 0
    k = 1
    term = 1 / (k + x) ** (3 / 2) - 1 / (k - x) ** (3 / 2)
    while abs(term) > error:
        sum_s += term
        k += 1
        term = 1 / (k + x) ** (3 / 2) - 1 / (k - x) ** (3 / 2)

    return [sum_s,k-1]


val1 = [0.5, 0.999999999]
for item in val1:
    print(f's({item}) = {s(item)[0]}')
    print(f'Б) {s(item)[1]}')
    print(f'B) time = {500*s(item)[1]} ms')
    print()
print(f'Г) 1 / k ** (3 / 2) - 3 * x / (2 * k ** (5 / 2))')  # для ускорения сходимости ряда
print()

def row_four(error=1e-10):
    sum_row = 0
    n = 1
    row = 1 / (n ** 2 + 1)
    while abs(row) > error:
        sum_row += row
        n += 1
        row = 1 / (n ** 2 + 1)

    return sum_row

print(row_four())
