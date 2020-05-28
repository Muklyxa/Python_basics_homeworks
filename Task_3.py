n = int(input("Enter a number 'n': "))

if n < 0:
    print("Number shoud be greater than zero!")
else:
    nn = int(str(f"{n}{n}"))
    nnn = int(str(f"{n}{n}{n}"))

    sum = n + nn +nnn

    print(f"The sum 'n + nn +nnn' is: {sum}")
