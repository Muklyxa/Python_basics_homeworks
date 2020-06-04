def my_func(x, y):
    """
    Function for exponentiation real positive number in integer negative power.
    If mantissa is zero the function will return 2^31!
    :param x:
    :param y:
    :return: res

    >>> my_func(2.5, -2)
    0.16
    """
    if x < 0:
        print("Mantissa is negative! Used abs.")
        x = -x
    if y > 0:
        print(f"Exponent is positive! Used -{y}.")
        y = -y

    res = 1.0
    for i in range(abs(y)):
        res = res * x

    try:
        res = 1.0 / res
    except ZeroDivisionError:
        print("Mantissa is too small!")
        res = 2 ** 31

    return res


try:
    print(my_func(float(input("Enter mantissa: ")),
                  int(input("Enter exponent: "))))
except ValueError:
    print("One of the arguments is not a number!")
