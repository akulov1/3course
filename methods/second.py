import math
def sign(x):
    if x>0:
        return 1
    return -1

def algo(a,b,c):
    x1 = -(b+sign(b)*math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = c/(a*x1)
    return f'x1 = {x1}, x2 = {x2}'

# def discriminant(a,b,c):


print(algo(1,-10**3,1))
print(algo(6,5,-4))
print(algo(6*10**30,5*10**30,-4*10**30))
print(algo(1.0000000, 4.0000000, 3.9999999))