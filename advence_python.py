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


