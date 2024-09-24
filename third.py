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


    if is_singular(m):
        print('Бесконечное множество решений')
        return

    # обратный ход
    x = [0 for i in range(n)]
    for k in range(n - 1, -1, -1):
        x[k] = (m[k][-1] - sum([m[k][j] * x[j] for j in range(k + 1, n)])) / m[k][k]

    for i in range(0,len(x)):
        print(f'x{i+1} = {x[i]}')
    return x


# проверка на невырожденность
def is_singular(m):
    for i in range(len(m)):
        if not m[i][i]:
            return True
    return False

def find_r(x,m):
    l = len(m)
    r=0
    result = [0 for i in range(len(x))]

    for i

    for i in range(0,len(x)):
        for j in range(0,len(m[i])-1):
            r += x[i]*m[i][j]
            print(m[i][j])
        result[i] = m[i][len(m[i])-1] - r
        print(m[i][len(m[i])-1])
        r = 0
    print(result)


m1 = [
    [10**-4,1,1],
    [1,2,4]
]

m2 = [
    [2.34,-4.21,-11.61,14.41],
    [8.04,5.22,0.27,-6.44],
    [3.92,-7.99,8.37,55.56]
]

m3 =[
    [4.43,-7.21,8.05,1.23,-2.56,2.62],
    [-1.29,6.47,2.96,3.22,6.12,-3.97],
    [6.12,8.31,9.41,1.78,-2.88,-9.12],
    [-2.57,6.93,-3.74,7.41,5.55,8.11],
    [1.46,3.62,7.83,6.25,-2.35,7.23]
]

res1 = solve_gauss(m1)
find_r(res1,m1)
print('\n')
res2 = solve_gauss(m2)
print('\n')
res3 = solve_gauss(m3)