import math
from my_fun_defs import quadratic
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a,b,c = map(int, input('请输入a,b,c:').split())
    print(quadratic(a, b, c))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
