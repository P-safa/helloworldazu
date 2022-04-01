def f(x):
    return x ** 3 - x ** 2 + 2
def df(x):
    return 3 * x ** 2 - 2 * x
def nr(x):
    h = f(x) / df(x)
    while abs(h) >= 0.000000001:
        h = f(x) / df(x)
        x = x - h
    print(x)
x0 = 28
nr(x0)