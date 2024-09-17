import math
import time


def erf(x, er=1e-8):
    sum_erf = 0
    term = x
    n = 0
    # while abs(term)>er:
    while True:
        old = sum_erf
        sum_erf += term
        if sum_erf == old:
            break
        n += 1
        term = (-1) ** n * (x ** (2 * n + 1)) / (math.factorial(n) * (2 * n + 1))
        # print(term, old)

    return 2 / math.pi ** (1 / 2) * sum_erf


values1 = [0.5, 1.0, 5.0, ]

# print('first_task:')
# for x in values1:
#     print(f'erf({x})={math.erf(x)}, {erf(x)}')
# print()


def phi(x, tol=5e-8):
    sum_phi = 0
    k = 1
    term = 1 / (k * (k + x))
    while abs(term) > tol:
        sum_phi += term
        k += 1
        term = 1 / (k * (k + x))
    return sum_phi

def phi2(x, tol=5e-8):
    sum_phi = 0
    k = 1
    term = 1-x / k*(k+x)*(k+1)
    while abs(term) > tol:
        sum_phi += term
        k += 1
        term = (1-x) / (k*(k+x)*(k+1))
    return sum_phi

x_values = [i * 0.1 for i in range(11)]
# st = time.time()
# for x in x_values:
#     print(f'phi({str(x)[:3]}) = {phi(x)}')
# e1 = time.time()
# print(e1-st)
#
# st2 = time.time()
# for x in x_values:
#     print(f'phi({str(x)[:3]}) = {phi2(x)}')
# e2 = time.time()
# print(e2-st2)

# print()
# print(f'ряд, который сходится быстрее: 1-x / k*(k+x)*(k+1)')
print()


def s(x, error=3e-8):
    sum_s = 0
    k = 1
    term = 1 / (k + x) ** (3 / 2) - 1 / (k - x) ** (3 / 2)
    while abs(term) > error:
        sum_s += term
        k += 1
        term = 1 / (k + x) ** (3 / 2) - 1 / (k - x) ** (3 / 2)

    return [sum_s, k - 1]


val1 = [0.5, 0.999999999]
for item in val1:
    print(f's({item}) = {s(item)[0]}')
    print(f'Б) {s(item)[1]}')
    # print(f'B) time = {500 * s(item)[1]} ms')
    print()

def s2(x, error=3e-8):
    sum_s = 0
    k = 1
    term = ((k - x) ** 3/2 + (k + x) ** 3/2) / ((k - x) ** 3/2 * (k + x) ** 3/2)
    while abs(term) > error:
        sum_s += term
        k += 1
        term = ((k - x) ** 3/2 + (k + x) ** 3/2) / ((k - x) ** 3/2 * (k + x) ** 3/2)

    return [sum_s, k - 1]

print(f'((k - x) ** 3/2 + (k + x) ** 3/2) / ((k - x) ** 3/2 * (k + x) ** 3/2)')  # для ускорения сходимости ряда
val1 = [0.5, 0.999999999]
# for item in val1:
    # print(f's({item}) = {s2(item)[0]}')
print({s2(val1[1])[1]})
print({s(val1[1])[1]})



def row_four1(error=1e-10):
    sum_row = 0
    n = 1
    row = 1 / (n ** 2 + 1)
    while abs(row) > error:
        sum_row += row
        n += 1
        row = 1 / (n ** 2 + 1)

    return sum_row,n


def row_four2(error=1e-10):
    sum_row = math.pi ** 2 / 6 - math.pi ** 4 / 90
    n = 1
    row = 1 / (n ** 4 * (n ** 2 + 1))
    while abs(row) > error:
        sum_row += row
        n += 1
        row = 1 / (n ** 4 * (n ** 2 + 1))

    return sum_row,n


# start1 = time.time()
# print(row_four1())
#
# start2 = time.time()
# print(row_four2())
# end2 = time.time()
# print(end2 - start2, end2, start2)
