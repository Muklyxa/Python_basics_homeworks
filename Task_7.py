def fact(n):
    result = 1
    for el in range(1, n + 1):
        result *= el
        yield result


try:
    n = int(input("Enter a positive number: "))
    if n < 0:
        print(f"{n} - is the negative number! {-n} will be used.")
        n = -n
    elif n == 0:
        print(1)

    for el in fact(n):
        print(el)
except ValueError:
    print("It's not a number!")
