def power(x, n = 2):
    # 如果没有指定参数，n 默认为 2
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s
"""
每一次都会增加一个 end 参数
def add_end(L = []):
    L.append('end')
    return L
"""
def add_end(L = []):
    if L is None:
        return []
    L.append('end')
    return L
# 但是调用需要组成一个list 或者 tuple
#calc([1,3,2,2])
def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

#可变参数形式
def calc(*number):
    sum = 0
    for n in number:
        sum += n
    return sum

#关键字参数
def person(name, age, **kw):
    print('name:',name, 'age:', age, 'other:', kw)

#变成可接收一个或多个数并计算乘积
#记住*number 是一个 tuple
def mul(*number):
    if len(number) == 0:
        raise TypeError('为空')
    sum = 1
    for n in number:
        sum *= n
    return sum