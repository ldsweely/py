import math
def quadratic_equation(a, b, c):
    if a==0:
        return(0,0)
    x1 = -b + math.sqrt(b*2 + 4*a*c)
    x2 = -b - math.sqrt(b*2 + 4*a*c)
    return(x1,x2)
print(quadratic_equation(2, 3, 0))
print(quadratic_equation(1, -6, 5))