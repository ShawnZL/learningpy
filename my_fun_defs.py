import math

def my_abs(x):
    # 此处举出不同不符合Type的样例
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def quadratic(a, b, c) ->[float, float]:
    #求解一元二次方程 ax^2 + bx + c = 0
    #输入多个数字map(function, input("").split())
    temp = math.sqrt(b * b - 4 * a * c)
    x = (-b + temp) / (2 * a)
    y = (-b - temp) / (2 * a)
    return x, y
