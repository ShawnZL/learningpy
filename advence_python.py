import builtins
from functools import reduce
def trim(s):
    i = 0; j = len(s);
    if len(s) == 0:
        return s
    else:
        while(s[i] == ' '):
            i += 1
        while(s[j - 1] == ' '):
            j -= 1
        res = s[i:j]
    return res

def findMinAndMax(L):
    if (len(L) == 0):
        return (None, None)
    elif (len(L) == 1):
        return (L[0], L[0])
    else:
        maxn = L[0]
        minn = L[0]
        for x in L:
            maxn = max(x, maxn)
            minn = min(x, minn)
        return (minn, maxn)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
"""
    高阶函数
"""
def add(x, y, f):
    return f(x) + f(y)
"""
    Map & Reduce
"""
"""
def f(x):
    return x * x

def fn(x, y):
    return x * 10 + y
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
"""
#整合进入一个函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
"""
    lambda函数简化
"""
def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

####
def normalize(name):
    return name.capotalize()
####
#####list求和
def prod(L):
    return reduce(lambda x, y: x * y, L)
#####
def str2float(s) -> float:
    s = s.split('.')
    if s[0]==0:
        return 0 + reduce(lambda x, y: x / 10 + y, map(lambda x:DIGITS[x], s[1][::-1]))/10
    #[::-1]表示为反转
    else:
        return reduce(lambda x, y: x * 10 + y, map(lambda x:DIGITS[x], s[0])) + reduce(lambda x, y: x / 10 + y, map(lambda x:DIGITS[x], s[1][::-1]))/10
