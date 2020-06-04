def my_func(val_1, val_2, val_3):
    """
    Function for finding sum of two maximal values.
    :param val_1:
    :param val_2:
    :param val_3:
    :return: res

    >>> my_func(1.0, 2.0, 3.0)
    5.0
    """
    try:
        args_list = [float(val_1), float(val_2), float(val_3)]
        args_list.remove(min(args_list))
        res = sum(args_list)
    except ValueError:
        print("One of values isn't numbers!")
        res = 0
    return res


print(my_func(input("Enter first value: "),
              input("Enter second value: "),
              input("Enter third value: ")))
