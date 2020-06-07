from functools import reduce


def mult(var1, var2):
    return var1 * var2


print(reduce(mult, [el for el in range(100, 1001) if (el % 2) == 0]))