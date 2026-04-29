import dis

def f(x):
    return x + 1

dis.dis(f)
print(f.__code__.co_consts)
print(f.__code__.co_varnames)