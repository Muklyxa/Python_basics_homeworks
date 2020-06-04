def div(dividend, divider):
    """
    Function for dividing a divisible by a divisor.
    In case zero division error will return 2^31.
    :param dividend:
    :param divider:
    :return: result of division

    >>> div(10.0, 5.0)
    2.0
    """
    try:
        res = dividend / divider
    except ZeroDivisionError:
        print("Zero Division Error! The result was overflowed!")
        res = 2**31
    return res


try:
    print(div(float(input("Enter dividend: ")), float(input("Enter divider: "))))
except ValueError:
    print("Printed value isn't number!")
