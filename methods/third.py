import math

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
def bubble_max_row(m, col):
    max_element = m[col][col]
    max_row = col
    for i in range(col + 1, len(m)):
        if abs(m[i][col]) > abs(max_element):
            max_element = m[i][col]
            max_row = i
    if max_row != col:
        m[col], m[max_row] = m[max_row], m[col]


def solve_gauss(m):
    n = len(m)
    # прямой ход
    for k in range(n - 1):
        bubble_max_row(m, k)
        for i in range(k + 1, n):
            div = m[i][k] / m[k][k]
            m[i][-1] -= div * m[k][-1]
            for j in range(k, n):
                m[i][j] -= div * m[k][j]

    for i in range(n):
        for j in range(len(m[i])):
            m[i][j] = round(m[i][j], 6)


    # if is_singular(m):
    #     for i in range(n):
    #         if m[i][i]==0:
    #             print(f'x{i+1}')
    #             zero = i

        # print(m)

    # обратный ход
    x = [0 for i in range(n)]
    for k in range(n - 1, -1, -1):
        if m[k][k]!=0 and m[k][k]!='constant':
            x[k] = ((m[k][-1] - sum([m[k][j] * x[j] for j in range(k + 1, n) if x[j]!='constant'])) / m[k][k])
        if m[k][k]==0:
            x[k] = 'constant'

    for i in range(n):
        if x[i]=='constant':
            for k in range(n):
                if i!=k:
                    x[k] = f'{x[k]}*{x[i]}'


    for i in range(0, len(x)):
        print(f'x{i + 1} = {x[i]}')
    return x


# проверка на невырожденность
def is_singular(m):
    for i in range(len(m)):
        if not m[i][i]:
            return True
    return False


def find_r(x, m):
    l = len(m)
    r = 0
    result = [0 for i in range(len(x))]
    temp = 0
    for i in range(0, len(m)):
        for j in range(0, len(x)):
            temp += m[i][j] * x[j]
        result[i] = m[i][len(m[i]) - 1] - temp
        temp = 0
    print(result)



m1 = [
    [10 ** -4, 1, 1],
    [1, 2, 4]
]

m2 = [
    [2.34, -4.21, -11.61, 14.41],
    [8.04, 5.22, 0.27, -6.44],
    [3.92, -7.99, 8.37, 55.56]
]

m3 = [
    [4.43, -7.21, 8.05, 1.23, -2.56, 2.62],
    [-1.29, 6.47, 2.96, 3.22, 6.12, -3.97],
    [6.12, 8.31, 9.41, 1.78, -2.88, -9.12],
    [-2.57, 6.93, -3.74, 7.41, 5.55, 8.11],
    [1.46, 3.62, 7.83, 6.25, -2.35, 7.23]
]


# res1 = solve_gauss(m1)
# find_r(res1,m1)
# print('\n')
# res2 = solve_gauss(m2)
# find_r(res2,m2)
# print('\n')
# res3 = solve_gauss(m3)
# find_r(res3,m3)
# print('\n')


def rank(matrix):
    size = len(matrix)
    size_rashiren = len(matrix)
    for i in range(size):
        if matrix[i][i]==0:
            size_rashiren-=1
    return f'Количество свободных переменных: {size-size_rashiren}'

def determinant(m):
    return m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1] - m[2][0]*m[1][1]*m[0][2] - m[2][1]*m[1][2]*m[0][0] - m[2][2]*m[1][0]*m[0][1]

m4 = [
    [1.00, 0.8, 0.64, erf(0.8)],
    [1.00, 0.90, 0.81, erf(0.90)],
    [1.00, 1.10, 1.21, erf(1.10)]
]
res4 = solve_gauss(m4)
print(f'Сумма х1, х2, х3: {sum(res4)}, erf(1.0): {math.erf(1)}')
print('\n')


m5 = [
    [0.1, 0.2, 0.3, 0.1],
    [0.4, 0.5, 0.6, 0.3],
    [0.7, 0.8, 0.9, 0.5]
]

print(f'Определитель = {determinant(m5)}')
res5 = solve_gauss(m5)
print(rank(m5))
print(m5)
